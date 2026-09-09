from collections import deque

import pytest

from snake_game_client.game.maps import AVAILABLE_MAPS


def _reachable_cells(game_map):
    start = game_map.start_positions[0]
    visited = {start}
    queue = deque([start])
    while queue:
        x, y = queue.popleft()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            neighbor = (x + dx, y + dy)
            if neighbor in visited or neighbor in game_map.walls:
                continue
            nx, ny = neighbor
            if not (0 <= nx < game_map.width and 0 <= ny < game_map.height):
                continue
            visited.add(neighbor)
            queue.append(neighbor)
    return visited


@pytest.mark.parametrize("game_map", AVAILABLE_MAPS, ids=lambda m: m.name)
def test_all_open_cells_are_reachable(game_map):
    open_cells = {
        (x, y)
        for x in range(game_map.width)
        for y in range(game_map.height)
        if (x, y) not in game_map.walls
    }
    assert _reachable_cells(game_map) == open_cells
