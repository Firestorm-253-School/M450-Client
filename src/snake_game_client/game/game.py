from ..ui.ui import Ui
from ..networking.client import GameClient
import pygame
import uuid

# 127.0.0.1 statt localhost: "localhost" braucht auf Windows oft 2+ Sekunden
# zum Verbinden (IPv6-Fallback-Verzögerung), 127.0.0.1 verbindet sofort.
SERVER_URL = "ws://127.0.0.1:8000/ws/game"

class Game:
  def __init__(self):
    pygame.init()

    pygame.mixer.music.load("assets/music/background.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    self.screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Snake Game")
    self.clock = pygame.time.Clock()

    # Eine Verbindung + Spieler-ID für die ganze Session, damit sie beim
    # mehrfachen Level-Start nicht immer neu aufgebaut wird (kein Leck,
    # konsistente Spieler-ID über mehrere Runden hinweg).
    player_id = str(uuid.uuid4())
    self.network = GameClient(f"{SERVER_URL}?player_id={player_id}")
    self.network.start()

    self.ui = Ui(self.screen, self.network)

  def run(self):
    running = True
    while running:
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              running = False

          self.ui.handle_event(event)

      self.ui.draw(self.screen)

      pygame.display.flip()
      self.clock.tick(60)
      
    pygame.quit()