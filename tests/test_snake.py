import pytest

from snake_game_client.game.maps import AVAILABLE_MAPS
from snake_game_client.game.snake import Snake


@pytest.mark.parametrize("game_map", AVAILABLE_MAPS, ids=lambda m: m.name)
def test_spawn_at_uses_solo_spawn_position(game_map):
    solo_spawn = game_map.start_for(0)
    snake = Snake.spawn_at(solo_spawn)
    assert snake.head() == solo_spawn


def test_spawn_at_creates_two_adjacent_segments():
    snake = Snake.spawn_at((5, 5))
    assert len(snake.body) == 2
    head_x, head_y = snake.body[0]
    tail_x, tail_y = snake.body[1]
    assert abs(head_x - tail_x) + abs(head_y - tail_y) == 1


@pytest.mark.parametrize("game_map", AVAILABLE_MAPS, ids=lambda m: m.name)
def test_spawn_at_every_spawn_position_avoids_walls(game_map):
    for position in game_map.start_positions:
        snake = Snake.spawn_at(position)
        for segment in snake.body:
            assert segment not in game_map.walls
