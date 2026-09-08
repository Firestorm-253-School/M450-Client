from .ui_element import UIElement
import pygame

class Button(UIElement):
  def __init__(self, rect, text, on_click, color=(255,255,255)):
    super().__init__(rect)

    self.text = text
    self.on_click = on_click
    self.color = color
    self.current_color = color

  def draw(self, screen: pygame.Surface):
    pygame.draw.rect(
      screen,
      self.current_color,
      self.rect,
      border_radius=8
      )

    font = pygame.font.Font(None, 32)
    text = font.render(self.text, True, (0, 0, 0))

    screen.blit(
      text,
      text.get_rect(center=self.rect.center)
    )

  def handle_event(self, event):
    if(event.type == pygame.MOUSEBUTTONDOWN):
      if(event.button == 1 and self.rect.collidepoint(event.pos)):
        self.on_click()


  def update(self):
    mouse_pos = pygame.mouse.get_pos()

    if(self.rect.collidepoint(mouse_pos)):
      self.current_color = tuple(int(c * 0.8) for c in self.color)

    else:
      self.current_color = self.color
