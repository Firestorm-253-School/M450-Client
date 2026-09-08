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

      image = pygame.image.load("assets/Snake_Game_Splash_Screen.png").convert_alpha()
      image = pygame.transform.scale(image, (self.screen.get_width(), self.screen.get_height()))

      self.screen.blit(image, (0, 0))


      pygame.display.flip()

      self.clock.tick(60)

    pygame.quit()
      
      
