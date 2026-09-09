from .screen import Screen
from ..ui_elements.button import Button
from ..ui_elements.label import Label

class LobbyScreen(Screen):

  def __init__(self, screen, game):

    title = Label(((screen.get_width() / 2), (screen.get_height() / 2) - 200), "Lobby", 72)
    label_players = Label(((screen.get_width() / 2), (screen.get_height() / 2) - 100), "Players (0)", 52)

    leave_button = Button(((screen.get_width() / 2) - 250, (screen.get_height() / 2) + 200, 200, 60), "Leave Lobby", lambda: game.ui.change_screen('main'), (255, 0, 0))
    start_button = Button(((screen.get_width() / 2) + 50, (screen.get_height() / 2) + 200, 200, 60), "Start Game", lambda: game.ui.change_screen('game'))

    self.ui_elements = {title, label_players, leave_button, start_button}

  def draw(self, screen):
    screen.fill((153, 217, 234))
    super().draw(screen)

