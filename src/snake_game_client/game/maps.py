from dataclasses import dataclass, field

@dataclass(frozen=True)
class Map:
    name: str
    width: int
    height: int
    walls: frozenset[tuple[int, int]]
    start_position: tuple[int, int]

def _border_walls(width: int, height: int) -> frozenset[tuple[int, int]]:
    walls = set()
    for x in range(width):
        walls.add((x, 0))
        walls.add((x, height -1))
    for y in range(height):
        walls.add((0, y))
        walls.add((width - 1, y))
    return frozenset(walls)

def _rect(x: int, y: int, width: int, height: int) -> frozenset[tuple[int, int]]:
    return frozenset((x + dx, y + dy) for dx in range(width) for dy in range(height))

CLASSIC = Map(
    name="Classic",
    width=24,
    height=18,
    walls=_border_walls(24, 18),
    start_position=(12, 9),
)

MEDIUM = Map(
    name="Medium",
    width=24,
    height=18,
    walls=(
        _border_walls(24, 18)
        | _rect(5, 3, 4, 1)   
        | _rect(5, 3, 1, 4)   
        | _rect(15, 3, 4, 1)  
        | _rect(18, 3, 1, 4)  
        | _rect(5, 14, 4, 1)  
        | _rect(5, 11, 1, 4)  
        | _rect(15, 14, 4, 1) 
        | _rect(18, 11, 1, 4) 
    ),
    start_position=(12, 9),
)

PRO = Map(
    name="Pro",
    width=24,
    height=18,
    walls=(
        _border_walls(24, 18)
        | _rect(2, 2, 20, 1)
        | _rect(2, 15, 20, 1)
        | _rect(2, 2, 1, 3)
        | _rect(2, 8, 1, 8)
        | _rect(21, 2, 1, 8)
        | _rect(21, 13, 1, 3)
        | _rect(7, 6, 10, 1)
        | _rect(7, 11, 10, 1)
        | _rect(7, 6, 1, 2)
        | _rect(7, 9, 1, 3)
        | _rect(16, 6, 1, 3)
        | _rect(16, 9, 1, 3)
    ),
    start_position=(12, 9)
)

AVAILABLE_MAPS: list[Map] = [
    CLASSIC,
    MEDIUM,
    PRO,
]