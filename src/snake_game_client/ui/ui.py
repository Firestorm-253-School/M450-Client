import pygame
from .main_menu import MainMenu

def test():
   print("Test")

class Ui:
  def __init__(self, screen): 
      self.main_menu = MainMenu(screen)


  def handle_event(self, event):
     self.main_menu.handle_event(event)

  def draw(self, screen): 
      self.main_menu.update()
      self.main_menu.draw(screen)
      
