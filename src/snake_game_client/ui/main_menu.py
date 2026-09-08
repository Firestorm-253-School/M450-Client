from .screen import Screen
from .button import Button
import pygame

class MainMenu(Screen):

  def __init__(self, screen):

    play_button = Button(((screen.get_width() / 2) - 100, (screen.get_height() / 2), 200, 60), "Play Game", lambda: print("Game started!"))

    self.ui_elements = {play_button}

  def update(self):
    for ui_element in self.ui_elements:
      ui_element.update()


  def handle_event(self, event):
    for ui_element in self.ui_elements:
      ui_element.handle_event(event)

  def draw(self, screen):
    image = pygame.image.load("assets/Snake_Game_Splash_Screen.png").convert_alpha()
    image = pygame.transform.scale(image, (screen.get_width(), screen.get_height()))
    screen.blit(image, (0, 0))

    for ui_element in self.ui_elements:
      ui_element.draw(screen)

