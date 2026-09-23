from dataclasses import dataclass
from .snake import Snake

@dataclass
class Player:
  username: str


@dataclass
class GamePlayer:
  uid: str
  snake: Snake
