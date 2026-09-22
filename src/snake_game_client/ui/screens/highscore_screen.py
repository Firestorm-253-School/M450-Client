from .screen import Screen
from ..ui_elements.button import Button
from ..ui_elements.label import Label

import json
import urllib.request

SERVER_URL = "http://127.0.0.1:8000/api/highscores"

class HighscoreScreen(Screen):

  def __init__(self, screen, change_screen):

    label = Label(((screen.get_width() / 2), (screen.get_height() / 2) - 200), "Highscores", 72)
    back_button = Button(((screen.get_width() / 2) - 100, (screen.get_height() / 2) + 260, 200, 60), "Zurueck", lambda: change_screen('main'))


    self.ui_elements = {label, back_button}

    with urllib.request.urlopen(SERVER_URL, timeout=3) as response:
      highscores = json.load(response)

    for index, entry in enumerate(highscores):
      text = f"{index + 1}.  {entry['name']}  -  {entry['score']}"
      self.ui_elements.add(Label(((screen.get_width() / 2), (screen.get_height() / 2) - 130 + index * 38), text, 40))

  def draw(self, screen):
    screen.fill((153, 217, 234))

    super().draw(screen)