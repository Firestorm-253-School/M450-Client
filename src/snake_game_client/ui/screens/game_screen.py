from .screen import Screen

from ...game.maps import CLASSIC, MEDIUM, PRO
from ...game.snake import Snake
from ..renderer import draw_map, draw_snake

import pygame

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

    super().handle_event(event)

  def draw(self, screen: pygame.Surface):
    screen.fill((153, 217, 234))

    draw_map(screen, self.map)
    draw_snake(screen, self.snake, self.map)
