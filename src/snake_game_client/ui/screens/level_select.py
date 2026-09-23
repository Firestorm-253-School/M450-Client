import pygame
from .screen import Screen
from ..ui_elements.button import Button
from ..ui_elements.label import Label

class LevelSelect(Screen):

  def __init__(self, screen, game):

    self.game = game

    label = Label(((screen.get_width() / 2), (screen.get_height() / 2) - 200), "Select Level", 72)
    level_classic = Button(((screen.get_width() / 2) - 100, (screen.get_height() / 2) - 100, 200, 60), "Classic", lambda: self.select_level('classic'))
    level_medium = Button(((screen.get_width() / 2) - 100, (screen.get_height() / 2), 200, 60), "Medium", lambda: self.select_level('medium'))
    level_pro = Button(((screen.get_width() / 2) - 100, (screen.get_height() / 2) + 100, 200, 60), "Pro", lambda: self.select_level('pro'))

    self.ui_elements = {label, level_classic, level_medium, level_pro}


  def select_level(self, level):
    self.game.network.send({"type": "create_game", "map": level})

    response = self.game.network.get_response("game_created")

    if(response["type"] == "game_created"):
      game_id = response["game_id"]
      self.game.ui.change_screen('game', {"map": level, "game_id": game_id})


  def draw(self, screen):
    screen.fill((153, 217, 234))

    super().draw(screen)

  def handle_event(self, event):
      if(event.type == pygame.KEYDOWN):
        if(event.key == pygame.K_ESCAPE):
          self.game.ui.change_screen('main')
  
      super().handle_event(event)

