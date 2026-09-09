from ..ui_elements.ui_element import UIElement

class Screen:

  ui_elements: list[UIElement] = {}

  def __init__(self, change_screen):
    pass

  def update(self):
    for ui_element in self.ui_elements:
      ui_element.update()

  def handle_event(self, event):
    for ui_element in self.ui_elements:
      ui_element.handle_event(event)

  def draw(self, screen):
    for ui_element in self.ui_elements:
          ui_element.draw(screen)