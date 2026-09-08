import pygame

class Game:

  def __init__(self):
      self.screen = pygame.display.set_mode((1280, 720))
      self.clock = pygame.time.Clock()
      pygame.init()


  def run(self):
    running = True
    while running:
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              running = False

      self.screen.fill("purple")

      pygame.display.flip()

      self.clock.tick(60)

    pygame.quit()
      
      
