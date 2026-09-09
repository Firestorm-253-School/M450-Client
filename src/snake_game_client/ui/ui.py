from .screens.main_menu import MainMenu
from .screens.game_screen import GameScreen
from .screens.level_select import LevelSelect

def test():
   print("Test")

class Ui:
  def __init__(self, screen):
      #self.main_menu = MainMenu(screen)
      self.screen = screen
      self.current_screen = MainMenu(self.screen, self.change_screen)

  def change_screen(self, screen, data = None):
     match screen:
        case 'main':
           self.current_screen = MainMenu(self.screen, self.change_screen)
        case 'game':
           self.current_screen = GameScreen(self.screen, self.change_screen, data)
        case 'level_select':
           self.current_screen = LevelSelect(self.screen, self.change_screen)
        
  def handle_event(self, event):
     self.current_screen.handle_event(event)

  def draw(self, screen): 
      self.current_screen.update()
      self.current_screen.draw(screen)
      
