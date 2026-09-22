from .screens.main_menu import MainMenu
from .screens.game_screen import GameScreen
from .screens.level_select import LevelSelect
from .screens.join_game import JoinGame
from .screens.welcome_screen import WelcomeScreen
from .screens.lobby_screen import LobbyScreen
from .screens.highscore_screen import HighscoreScreen


def test():
   print("Test")

class Ui:
  def __init__(self, screen, network, game):
      self.game = game
      self.screen = screen
      self.network = network
      self.current_screen = WelcomeScreen(self.screen, game)

  def change_screen(self, screen, data = None):
     match screen:
        case 'main':
           self.current_screen = MainMenu(self.screen, self.game)
        case 'game':
           self.current_screen = GameScreen(self.screen, self.game, data, self.network)
        case 'level_select':
           self.current_screen = LevelSelect(self.screen, self.game)
        case 'join_game':
           self.current_screen = JoinGame(self.screen, self.game)
        case 'lobby_screen':
           self.current_screen = LobbyScreen(self.screen, self.game)
         case 'highscore':
             self.current_screen = HighscoreScreen(self.screen, self.change_screen)

        
  def handle_event(self, event):
     self.current_screen.handle_event(event)

  def draw(self, screen): 
      self.current_screen.update()
      self.current_screen.draw(screen)
      
