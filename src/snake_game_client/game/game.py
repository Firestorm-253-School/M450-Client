from ..ui.ui import Ui
import pygame
from pathlib import Path

class Game:
  def __init__(self):
    pygame.init()

    pygame.mixer.music.load("assets/music/background.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
    
    self.screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Snake Game")
    self.clock = pygame.time.Clock()

    self.ui = Ui(self.screen, self)

    self.running = False

    self.player = None

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