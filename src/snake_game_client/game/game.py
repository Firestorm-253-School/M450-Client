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

    self.ui = Ui(self.screen)

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