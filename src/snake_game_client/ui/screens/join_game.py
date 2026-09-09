from .screen import Screen
from ..ui_elements.button import Button
from ..ui_elements.input import Input
from ..ui_elements.label import Label

class JoinGame(Screen):

  def __init__(self, screen, change_screen):

    self.title = Label(((screen.get_width() / 2), (screen.get_height() / 2) - 100), "Join Game", 72)

    self.key_input = Input(((screen.get_width() / 2) - 100, (screen.get_height() / 2) - 40, 200, 60), "Key")

    self.join_button = Button(((screen.get_width() / 2) - 100, (screen.get_height() / 2) + 40, 200, 60), "Join Game", lambda: change_screen('game', self.key_input.value))

    self.ui_elements = {self.title, self.key_input, self.join_button}

  def draw(self, screen):
    screen.fill((153, 217, 234))

    super().draw(screen)

  def update(self):
    self.join_button.disabled = not self.key_input.value
    super().update()
