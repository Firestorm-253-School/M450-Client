from .screen import Screen

from ...game.maps import CLASSIC, MEDIUM, PRO
from ...game.snake import Snake
from ..renderer import draw_map, draw_snake, draw_apples

from ..ui_elements.label import Label, Align
from ..ui_elements.button import Button
from ...game.player import PlayerData

import pyperclip
import pygame

DIRECTION_KEYS = {
  pygame.K_UP: (0, -1),
  pygame.K_DOWN: (0, 1),
  pygame.K_LEFT: (-1, 0),
  pygame.K_RIGHT: (1, 0),
}

DIRECTION_NAMES = {
  (0, -1): "up",
  (0, 1): "down",
  (-1, 0): "left",
  (1, 0): "right",
}

class GameScreen(Screen):

  def __init__(self, screen, game, data, network):
    self.game = game
    self.network = network

    match data["map"]:
      case 'classic':
        self.map = CLASSIC
        self.map_name = 'classic'
      case 'medium':
        self.map = MEDIUM
        self.map_name = 'medium'
      case 'pro':
        self.map = PRO
        self.map_name = 'pro'
      case _:
        self.map = CLASSIC
        self.map_name = 'classic'

    self.game_id = data["game_id"]

    self.game_id_label = Label((90, 30), self.game_id, 36, Align.START, (0,0,0))
    self.game_id_copy_button = Button((10, 10, 65, 40), "Copy", lambda: pyperclip.copy(self.game_id), (255,255,255),(230,230,230))

    self.ui_elements = {self.game_id_label, self.game_id_copy_button}

    self.snakes = {}
    
    self.game_over = False

    self.apples = []


  def handle_event(self, event: pygame.event.Event):
    if(event.type == pygame.KEYDOWN):
      if(event.key == pygame.K_ESCAPE):
        self.game.network.send({"type": "leave_game"})
        response = self.game.network.get_response("game_left")
        if(response != None):
          self.game.ui.change_screen('main')
      elif event.key in DIRECTION_KEYS:
        self._send_direction(DIRECTION_KEYS[event.key])

    super().handle_event(event)

  def _send_direction(self, direction: tuple[int, int]) -> None:
    self.network.send({"type": "set_direction", "direction": DIRECTION_NAMES[direction]})

  def apply_server_state(self, players: dict[str, PlayerData], apples) -> None:

    for player_id, player in players.items():
      if player_id in self.snakes:
        self.snakes[player_id].direction = player.direction
        self.snakes[player_id].body = player.body
      else:
        self.snakes[player_id] = Snake(player.body, player.direction)

      if(player_id == self.game.player.username):
        if(player.alive == False):
          self.game_over = True


    if(len(apples) < len(self.apples)):
      self.game.sound_bite.play()
    self.apples = apples


  def update(self):
    while not self.network.incoming.empty():
      message = self.network.incoming.get()
      if message.get("type") == "game_state":
        apples = [tuple(position) for position in message["apples"]]
        players = {
          player_id: PlayerData(
              body=[tuple(position) for position in data["snake"]],
              alive=data["alive"],
              direction=tuple(data["direction"])
          )
          for player_id, data in message["snakes"].items()
        }
        self.apply_server_state(players, apples)
      elif message.get("type") == "game_over":
        self.game_over = True

    super().update()

  def draw(self, screen: pygame.Surface):
    screen.fill((153, 217, 234))

    draw_map(screen, self.map)
    for snake in self.snakes.values():
      draw_snake(screen, snake, self.map)
    draw_apples(screen, self.apples, self.map)

    super().draw(screen)

    if self.game_over:
      self._draw_game_over(screen)

  def _draw_game_over(self, screen: pygame.Surface) -> None:
    overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 150))
    screen.blit(overlay, (0, 0))

    font = pygame.font.Font(None, 96)
    text = font.render("Game Over", True, "white")
    screen.blit(text, text.get_rect(center=screen.get_rect().center))
