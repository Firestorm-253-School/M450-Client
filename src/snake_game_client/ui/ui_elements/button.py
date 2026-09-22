from .ui_element import UIElement
import pygame

class Button(UIElement):
  def __init__(self, rect, text, on_click, color=(255,255,255), color_hover=(200,200,200), color_disabled=(150, 150, 150)):
    super().__init__(rect)

    self.text = text
    self.on_click = on_click

    self.color = color
    self.color_hover = color_hover
    self.color_disabled = color_disabled

    self.disabled = False
    self.hover = False

  def draw(self, screen: pygame.Surface):
    color = self.color_disabled if self.disabled else (self.color_hover if self.hover else self.color) 

    pygame.draw.rect(
      screen,
      color,
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
    if(event.type == pygame.MOUSEBUTTONDOWN and not self.disabled):
      if(event.button == 1 and self.rect.collidepoint(event.pos)):
        self.on_click()


  def update(self):
    mouse_pos = pygame.mouse.get_pos()
    self.hover = self.rect.collidepoint(mouse_pos)