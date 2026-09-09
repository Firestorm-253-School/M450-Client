from .screen import Screen

from ...game.maps import CLASSIC, MEDIUM, PRO
from ...game.snake import Snake
from ..renderer import draw_map, draw_snake

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

  def __init__(self, screen, change_screen, data, network):
    self.change_screen = change_screen
    self.ui_elements = {}
    self.network = network
    match data:
      case 'classic':
        self.map = CLASSIC
      case 'medium':
        self.map = MEDIUM
      case 'pro':
        self.map = PRO
      case _:
        self.map = CLASSIC

    # TODO Multiplayer: aktuell nur Spieler 0 (Solo). Für mehrere Spieler:
    # eine Liste von Snakes anlegen, je eine pro Spieler-Index via self.map.start_for(i).
    self.snake = Snake.spawn_at(self.map.start_for(0))
    self.game_over = False

    self.network.send({"type": "create_game"})


  def handle_event(self, event: pygame.event.Event):
    if(event.type == pygame.KEYDOWN):
      if(event.key == pygame.K_ESCAPE):
        self.change_screen('main')
      elif event.key in DIRECTION_KEYS:
        self._send_direction(DIRECTION_KEYS[event.key])

    super().handle_event(event)

  def _send_direction(self, direction: tuple[int, int]) -> None:
    self.network.send({"type": "set_direction", "direction": DIRECTION_NAMES[direction]})

  def apply_server_state(self, body: list[tuple[int, int]]) -> None:
    if body and self.snake.body:
      old_head = self.snake.body[0]
      new_head = body[0]
      moved = (new_head[0] - old_head[0], new_head[1] - old_head[1])
      if moved != (0, 0):
        self.snake.direction = moved

    self.snake.body = body

  def update(self):
    while not self.network.incoming.empty():
      message = self.network.incoming.get()
      if message.get("type") == "game_state":
        body = [tuple(position) for position in message["snake"]]
        self.apply_server_state(body)
      elif message.get("type") == "game_over":
        self.game_over = True

    super().update()

  def draw(self, screen: pygame.Surface):
    screen.fill((153, 217, 234))

    draw_map(screen, self.map)
    draw_snake(screen, self.snake, self.map)

    if self.game_over:
      self._draw_game_over(screen)

  def _draw_game_over(self, screen: pygame.Surface) -> None:
    overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 150))
    screen.blit(overlay, (0, 0))

    font = pygame.font.Font(None, 96)
    text = font.render("Game Over", True, "white")
    screen.blit(text, text.get_rect(center=screen.get_rect().center))
