from dataclasses import dataclass
from .snake import Snake

@dataclass
class Player:
  username: str


@dataclass
class GamePlayer:
  uid: str
  snake: Snake


@dataclass
class PlayerData:
    body: list[tuple[int, int]]
    alive: bool
    direction: tuple[int, int]
    color: str