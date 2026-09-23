from ..ui.ui import Ui
from ..networking.client import GameClient
import pygame

# 127.0.0.1 statt localhost: "localhost" braucht auf Windows oft 2+ Sekunden
# zum Verbinden (IPv6-Fallback-Verzögerung), 127.0.0.1 verbindet sofort.
SERVER_URL = "ws://127.0.0.1:8000/ws/game"

class Game:
  def __init__(self):
    pygame.init()

    pygame.mixer.music.load("assets/music/background.mp3")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)

    self.sound_bite = pygame.mixer.Sound("assets/sounds/bite.mp3")

    self.screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Snake Game")
    self.clock = pygame.time.Clock()

    self.network = None
    self.player = None

    self.ui = Ui(self.screen, self)

    self.running = False


  def run(self):
    self.running = True
    while self.running:
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              self.quit()

          self.ui.handle_event(event)

      self.ui.draw(self.screen)

      pygame.display.flip()
      self.clock.tick(60)
      
    pygame.quit()

  def quit(self):
     self.running = False

  def init_network(self, player):
    self.player = player
    self.network = GameClient(f"{SERVER_URL}?player_id={self.player.username}")
    self.network.start()