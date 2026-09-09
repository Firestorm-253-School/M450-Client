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

class GameScreen(Screen):

  def __init__(self, screen, change_screen, data):
    self.change_screen = change_screen
    self.ui_elements = {}
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


  def handle_event(self, event: pygame.event.Event):
    if(event.type == pygame.KEYDOWN):
      if(event.key == pygame.K_ESCAPE):
        self.change_screen('main')
      elif event.key in DIRECTION_KEYS:
        self._send_direction(DIRECTION_KEYS[event.key])

    super().handle_event(event)

  def _send_direction(self, direction: tuple[int, int]) -> None:
    # TODO Netzwerk: hier später die Richtung an den Server schicken.
    # Aktuell nur Platzhalter, tut noch nichts (Bewegung entscheidet der Server).
    pass

  def apply_server_state(self, body: list[tuple[int, int]]) -> None:
    # TODO Netzwerk: wird von der Netzwerk-Schicht aufgerufen, sobald der
    # Server eine neue Snake-Position schickt (Bewegung, Wachstum, etc.).
    self.snake.body = body

  def draw(self, screen: pygame.Surface):
    screen.fill((153, 217, 234))

    draw_map(screen, self.map)
    draw_snake(screen, self.snake, self.map)
