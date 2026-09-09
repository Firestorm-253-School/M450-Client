import pygame

from snake_game_client.game.maps import Map
from snake_game_client.game.snake import Snake

CELL_SIZE = 40
BACKGROUND_LIGHT = "#AAD751"
BACKGROUND_DARK = "#94C538"
WALL_COLOR = "#537A32"
# TODO Multiplayer: bis zu 4 Snakes gleichzeitig, jede braucht eine eigene,
# klar unterscheidbare Farbe statt dieser einen fest verdrahteten.
SNAKE_COLOR = "#3477DB"
SNAKE_OUTLINE_COLOR = "#255A9E"


def _offsets(screen: pygame.Surface, game_map: Map) -> tuple[float, float]:
    offset_x = (screen.get_width() - (game_map.width * CELL_SIZE)) / 2
    offset_y = (screen.get_height() - (game_map.height * CELL_SIZE)) / 2
    return offset_x, offset_y


def _cell_rect(x: int, y: int, offset_x: float, offset_y: float) -> pygame.Rect:
    return pygame.Rect(offset_x + x * CELL_SIZE, offset_y + y * CELL_SIZE, CELL_SIZE, CELL_SIZE)


def draw_map(screen: pygame.Surface, game_map: Map) -> None:
    offset_x, offset_y = _offsets(screen, game_map)

    for y in range(game_map.height):
        for x in range(game_map.width):
            color = BACKGROUND_LIGHT if (x + y) % 2 == 0 else BACKGROUND_DARK
            pygame.draw.rect(screen, color, _cell_rect(x, y, offset_x, offset_y))

    for x, y in game_map.walls:
        pygame.draw.rect(screen, WALL_COLOR, _cell_rect(x, y, offset_x, offset_y))


def _connector_rect(rect1: pygame.Rect, rect2: pygame.Rect) -> pygame.Rect:
    if rect1.centery == rect2.centery:
        left = min(rect1.centerx, rect2.centerx)
        right = max(rect1.centerx, rect2.centerx)
        return pygame.Rect(left, rect1.top, right - left, rect1.height)

    top = min(rect1.centery, rect2.centery)
    bottom = max(rect1.centery, rect2.centery)
    return pygame.Rect(rect1.left, top, rect1.width, bottom - top)


def draw_snake(screen: pygame.Surface, snake: Snake, game_map: Map) -> None:
    offset_x, offset_y = _offsets(screen, game_map)

    # Verbindungsstücke reichen nur von der Zellenmitte zur Zellenmitte,
    # damit die echten Enden (Kopf/Schwanz) rund bleiben statt zugemalt zu werden.
    for (x1, y1), (x2, y2) in zip(snake.body, snake.body[1:]):
        connector = _connector_rect(
            _cell_rect(x1, y1, offset_x, offset_y),
            _cell_rect(x2, y2, offset_x, offset_y),
        )
        pygame.draw.rect(screen, SNAKE_COLOR, connector)

    for x, y in snake.body:
        rect = _cell_rect(x, y, offset_x, offset_y)
        pygame.draw.rect(screen, SNAKE_COLOR, rect, border_radius=12)

    head_rect = _cell_rect(*snake.head(), offset_x, offset_y)
    pygame.draw.rect(screen, SNAKE_OUTLINE_COLOR, head_rect, width=2, border_radius=12)

    _draw_face(screen, snake, offset_x, offset_y)


def _draw_face(screen: pygame.Surface, snake: Snake, offset_x: float, offset_y: float) -> None:
    head_x, head_y = snake.head()
    center_x = offset_x + head_x * CELL_SIZE + CELL_SIZE / 2
    center_y = offset_y + head_y * CELL_SIZE + CELL_SIZE / 2

    dx, dy = snake.direction
    perp_x, perp_y = -dy, dx

    forward = CELL_SIZE * 0.1
    sideways = CELL_SIZE * 0.2
    eye_radius = CELL_SIZE * 0.17
    pupil_radius = eye_radius * 0.55
    shine_radius = pupil_radius * 0.4

    for side in (-1, 1):
        eye_x = center_x + dx * forward + perp_x * side * sideways
        eye_y = center_y + dy * forward + perp_y * side * sideways
        pygame.draw.circle(screen, "white", (eye_x, eye_y), eye_radius)
        pupil_x = eye_x + dx * pupil_radius * 0.7
        pupil_y = eye_y + dy * pupil_radius * 0.7
        pygame.draw.circle(screen, "black", (pupil_x, pupil_y), pupil_radius)
        shine_x = pupil_x - pupil_radius * 0.4
        shine_y = pupil_y - pupil_radius * 0.4
        pygame.draw.circle(screen, "white", (shine_x, shine_y), shine_radius)
