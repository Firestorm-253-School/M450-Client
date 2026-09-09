import pytest

from snake_game_client.game.maps import AVAILABLE_MAPS, CLASSIC


@pytest.mark.parametrize("game_map", AVAILABLE_MAPS, ids=lambda m: m.name)
def test_map_has_four_start_positions(game_map):
    assert len(game_map.start_positions) == 4


@pytest.mark.parametrize("game_map", AVAILABLE_MAPS, ids=lambda m: m.name)
def test_start_positions_are_not_walls(game_map):
    for position in game_map.start_positions:
        assert position not in game_map.walls


@pytest.mark.parametrize("game_map", AVAILABLE_MAPS, ids=lambda m: m.name)
def test_start_positions_are_within_bounds(game_map):
    for x, y in game_map.start_positions:
        assert 0 <= x < game_map.width
        assert 0 <= y < game_map.height


@pytest.mark.parametrize("game_map", AVAILABLE_MAPS, ids=lambda m: m.name)
def test_border_is_fully_walled(game_map):
    for x in range(game_map.width):
        assert (x, 0) in game_map.walls
        assert (x, game_map.height - 1) in game_map.walls
    for y in range(game_map.height):
        assert (0, y) in game_map.walls
        assert (game_map.width - 1, y) in game_map.walls


def test_map_names_are_unique():
    names = [m.name for m in AVAILABLE_MAPS]
    assert len(names) == len(set(names))


def test_classic_interior_has_no_walls():
    for x in range(1, CLASSIC.width - 1):
        for y in range(1, CLASSIC.height - 1):
            assert (x, y) not in CLASSIC.walls
