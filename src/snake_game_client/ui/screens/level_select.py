from .screen import Screen
from ..ui_elements.button import Button
from ..ui_elements.label import Label

class LevelSelect(Screen):

  def __init__(self, screen, game):

    label = Label(((screen.get_width() / 2), (screen.get_height() / 2) - 200), "Select Level", 72)
    level_classic = Button(((screen.get_width() / 2) - 100, (screen.get_height() / 2) - 100, 200, 60), "Classic", lambda: game.ui.change_screen('game', 'classic'))
    level_medium = Button(((screen.get_width() / 2) - 100, (screen.get_height() / 2), 200, 60), "Medium", lambda: game.ui.change_screen('game', 'medium'))
    level_pro = Button(((screen.get_width() / 2) - 100, (screen.get_height() / 2) + 100, 200, 60), "Pro", lambda: game.ui.change_screen('game', 'pro'))

    self.ui_elements = {label, level_classic, level_medium, level_pro}

  def draw(self, screen):
    screen.fill((153, 217, 234))

    super().draw(screen)

