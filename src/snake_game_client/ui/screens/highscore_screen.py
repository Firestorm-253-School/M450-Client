from .screen import Screen
from ..ui_elements.button import Button
from ..ui_elements.label import Label

import json
import urllib.request

SERVER_URL = "http://127.0.0.1:8000/api/highscores"

MODI = ["classic", "medium", "pro"]
AKTIV = (255, 240, 0)

class HighscoreScreen(Screen):

  def __init__(self, screen, change_screen, modus=None):
    self.screen = screen
    self.change_screen = change_screen

    self.zeige(modus)

  def zeige(self, modus):
    screen = self.screen
    mitte_x = screen.get_width() / 2
    mitte_y = screen.get_height() / 2

    titel = "Highscores" if modus is None else f"Highscores: {modus}"
    elemente = {
      Label((mitte_x, mitte_y - 250), titel, 72),
      Button((mitte_x - 100, mitte_y + 260, 200, 60), "Zurueck", lambda: self.change_screen('main')),
    }

    for index, name in enumerate([None, *MODI]):
      x = mitte_x - 420 + index * 215
      beschriftung = "Alle" if name is None else name
      farbe = AKTIV if name == modus else (255, 255, 255)
      elemente.add(Button((x, mitte_y - 180, 195, 50), beschriftung, lambda name=name: self.zeige(name), farbe))

    uebersicht = self.lade_uebersicht(modus)

    if uebersicht["hinweis"]:
      elemente.add(Label((mitte_x, mitte_y), uebersicht["hinweis"], 40))

    for index, eintrag in enumerate(uebersicht["highscore"]):
      text = f"{index + 1}.  {eintrag['name']}  :  {eintrag['score']}"
      if modus is None:
        text += f"  ({eintrag['modus']})"
      elemente.add(Label((mitte_x, mitte_y - 90 + index * 38), text, 40))

    self.ui_elements = elemente

  def lade_uebersicht(self, modus):
    url = SERVER_URL if modus is None else f"{SERVER_URL}?modus={modus}"
    try:
      with urllib.request.urlopen(url, timeout=3) as response:
        return json.load(response)
    except Exception:
      return {"highscore": [], "hinweis": "Server nicht erreichbar"}

  def draw(self, screen):
    screen.fill((153, 217, 234))
    super().draw(screen)