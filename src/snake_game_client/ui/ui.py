import pygame
from .main_menu import MainMenu

def test():
   print("Test")

class Ui:
  def __init__(self):

      
      self.screen = pygame.display.set_mode((1280, 720))
      pygame.display.set_caption("Snake Game")
      self.clock = pygame.time.Clock()
      pygame.init()

      self.main_menu = MainMenu(self.screen)


  def run(self):

    running = True
    while running:
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              running = False

          self.main_menu.handle_event(event)

      self.main_menu.update()
      self.main_menu.draw(self.screen)

      pygame.display.flip()

      self.clock.tick(60)

    pygame.quit()
      
