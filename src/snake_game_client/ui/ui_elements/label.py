from .ui_element import UIElement
import pygame

class Label(UIElement):
  def __init__(self, pos, text, font_size, color=(255,255,255)):
    self.pos = pos
    self.text = text
    self.font_size = font_size
    self.color = color
    self.current_color = color

  def draw(self, screen: pygame.Surface):
    font = pygame.font.Font(None, self.font_size)
    text = font.render(self.text, True, (0, 0, 0))

    screen.blit(
      text,
      text.get_rect(center=self.pos)
    )
