from .screen import Screen
from ..ui_elements.button import Button
from ..ui_elements.label import Label
from ..ui_elements.input import Input
from ...game.player import Player
import pygame

class WelcomeScreen(Screen):

  def __init__(self, screen, game):
    self.game = game

    title = Label(((screen.get_width() / 2), 50), "Welcome, Please Enter your Username", 72)
    self.username_input = Input(((screen.get_width() / 2) - 100, (screen.get_height() / 2), 200, 60), "Username")
    self.confirm_button = Button(((screen.get_width() / 2) - 100, (screen.get_height() / 2) + 80, 200, 60), "Confirm", lambda: self.set_username(self.username_input.value))

    self.ui_elements = {title, self.username_input, self.confirm_button}

  def draw(self, screen):
    image = pygame.image.load("assets/Snake_Game_Splash_Screen.png").convert_alpha()
    image = pygame.transform.scale(image, (screen.get_width(), screen.get_height()))
    screen.blit(image, (0, 0))

    super().draw(screen)

  def update(self):
    self.confirm_button.disabled = not self.username_input.value

    super().update()

  def set_username(self, username):
    player = Player(username)
    self.game.player = player

    self.game.ui.change_screen('main')

