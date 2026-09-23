import pygame
from .screen import Screen
from ..ui_elements.button import Button
from ..ui_elements.input import Input
from ..ui_elements.label import Label

class JoinGame(Screen):

  def __init__(self, screen, game):

    self.game = game

    self.title = Label(((screen.get_width() / 2), (screen.get_height() / 2) - 100), "Join Game", 72)

    self.key_input = Input(((screen.get_width() / 2) - 100, (screen.get_height() / 2) - 40, 200, 60), "Key")

    self.join_button = Button(((screen.get_width() / 2) - 100, (screen.get_height() / 2) + 40, 200, 60), "Join Game", self.join_game)

    self.ui_elements = {self.title, self.key_input, self.join_button}

  def join_game(self):
    self.game.network.send({"type": "join_game", "game_id": self.key_input.value})

    response = self.game.network.get_response("game_join_failed", "game_joined")

    if(response["type"] == 'game_join_failed'):
      pass
    elif(response["type"] == 'game_joined'):
      game_id = response["game_id"]
      map = response["map"]
      self.game.ui.change_screen('game', {"map": map, "game_id": game_id})


  def draw(self, screen):
    screen.fill((153, 217, 234))

    super().draw(screen)

  def update(self):
    self.join_button.disabled = not self.key_input.value
    super().update()

  def handle_event(self, event):
    if(event.type == pygame.KEYDOWN):
      if(event.key == pygame.K_ESCAPE):
        self.game.ui.change_screen('main')

    super().handle_event(event)