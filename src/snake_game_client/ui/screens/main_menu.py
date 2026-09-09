from .screen import Screen
from ..ui_elements.button import Button
import pygame

class MainMenu(Screen):

  def __init__(self, screen, change_screen):

    play_button = Button(((screen.get_width() / 2) - 100, (screen.get_height() / 2), 200, 60), "Play Game", lambda: change_screen('level_select'))
    quit_button = Button(((screen.get_width() / 2) - 100, (screen.get_height() / 2) + 80, 200, 60), "Quit", lambda: pygame.quit(), (255, 0, 0))

    self.ui_elements = {play_button, quit_button}

  def draw(self, screen):
    image = pygame.image.load("assets/Snake_Game_Splash_Screen.png").convert_alpha()
    image = pygame.transform.scale(image, (screen.get_width(), screen.get_height()))
    screen.blit(image, (0, 0))

    super().draw(screen)

