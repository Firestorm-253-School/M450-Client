from .ui_element import UIElement
from enum import Enum
import pygame


class Align(Enum):
  START = 'start'
  CENTER = 'center'
  END = 'end'

class Label(UIElement):
  def __init__(self, pos, text, font_size, align=Align.CENTER, color=(0, 0, 0)):
    self.pos = pos
    self.text = text
    self.font_size = font_size
    self.color = color

    self.align = align

  def draw(self, screen: pygame.Surface):
    font = pygame.font.Font(None, self.font_size)
    text = font.render(self.text, True, self.color)

    text.get_rect()

    match self.align.value:
      case 'start':
        rect = text.get_rect(midleft=self.pos)
      case 'center':
        rect = text.get_rect(center=self.pos)
      case 'end':
        rect = text.get_rect(midright=self.pos)

    screen.blit(
      text,
      rect
    )
