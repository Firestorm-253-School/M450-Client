import pygame

class UIElement:
  def __init__(self, rect):
    self.rect = pygame.Rect(rect)

  def draw(self, screen):
    pass

  def handle_event(self, event):
    pass

  def update(self):
    pass