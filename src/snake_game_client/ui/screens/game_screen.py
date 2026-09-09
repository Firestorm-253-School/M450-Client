from .screen import Screen

from ...game.maps import CLASSIC, MEDIUM, PRO
from ..renderer import draw_map

import pygame

class GameScreen(Screen):

  def __init__(self, screen, game, data):
    self.game = game
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


  def handle_event(self, event: pygame.event.Event):
    if(event.type == pygame.KEYDOWN):
      if(event.key == pygame.K_ESCAPE):
        self.game.ui.change_screen('main')

    super().handle_event(event)

  def draw(self, screen: pygame.Surface):
    screen.fill((153, 217, 234))

    draw_map(screen, self.map)
