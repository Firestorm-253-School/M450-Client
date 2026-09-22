from .ui_element import UIElement
import pygame

class Input(UIElement):
  def __init__(self, rect, placeholder):
    super().__init__(rect)

    self.placeholder = placeholder
    self.value = ""
    self.active = False

    self.color_active = (30, 30, 30)
    self.color_inactive = (255, 255, 255)

    self.font = pygame.font.Font(None, 32)


  def draw(self, screen: pygame.Surface):
    color = self.color_active if self.active else self.color_inactive

    pygame.draw.rect(screen, (200, 200, 200), self.rect, border_radius=10)
    pygame.draw.rect(screen, color, self.rect, 2, border_radius=10)

    if(self.value):
       value = self.value
       color = (0, 0, 0)
    else:
       value = self.placeholder
       color = (100, 100, 100)
       
    text = self.font.render(value, True, color)

    screen.blit(
        text,
        (self.rect.x + 10, self.rect.centery - 10)
    )

  def handle_event(self, event):
    if event.type == pygame.MOUSEBUTTONDOWN:
      self.active = self.rect.collidepoint(event.pos)

    if event.type == pygame.KEYDOWN and self.active:
        if event.key == pygame.K_BACKSPACE:
            self.value = self.value[:-1]
        elif event.key == pygame.K_RETURN:
            return self.value
        else:
            self.value += event.unicode
    return None
