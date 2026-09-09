from .screen import Screen
from ..ui_elements.button import Button
from ..ui_elements.label import Label, Align
import pygame

class MainMenu(Screen):

  def __init__(self, screen, game):

    host_button = Button(((screen.get_width() / 2) - 100, (screen.get_height() / 2), 200, 60), "Host Game", lambda: game.ui.change_screen('level_select'))
    join_button = Button(((screen.get_width() / 2) - 100, (screen.get_height() / 2) + 80, 200, 60), "Join Game", lambda: game.ui.change_screen('join_game'))
    quit_button = Button(((screen.get_width() / 2) - 100, (screen.get_height() / 2) + 160, 200, 60), "Quit", lambda: game.quit(), (255, 0, 0))

    current_player_label = Label(((screen.get_width() / 2) + 150, (screen.get_height() / 2)), "Player", 42, align=Align.START)
    player_label = Label(((screen.get_width() / 2) + 150, (screen.get_height() / 2) + 40), "Username: " + game.player.username, 36, color=(255,240,0), align=Align.START)

    self.ui_elements = {host_button, join_button, quit_button, current_player_label, player_label}

  def draw(self, screen):
    image = pygame.image.load("assets/Snake_Game_Splash_Screen.png").convert_alpha()
    image = pygame.transform.scale(image, (screen.get_width(), screen.get_height()))
    screen.blit(image, (0, 0))

    super().draw(screen)

