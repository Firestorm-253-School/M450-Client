import pygame

from snake_game_client.game.maps import Map

CELL_SIZE = 40
BACKGROUND_LIGHT = "#AAD751"
BACKGROUND_DARK = "#94C538"
WALL_COLOR = "#537A32"

def draw_map(screen: pygame.Surface, game_map: Map) -> None:

    offset_x = (screen.get_width() - (game_map.width * CELL_SIZE)) / 2
    offset_y = (screen.get_height() - (game_map.height * CELL_SIZE)) / 2

    for y in range(game_map.height):
        for x in range(game_map.width):
            color = BACKGROUND_LIGHT if (x + y) % 2 == 0 else BACKGROUND_DARK
            rect = pygame.Rect(offset_x + x * CELL_SIZE, y * CELL_SIZE, offset_y + CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, color, rect)

    for x, y in game_map.walls:
        rect = pygame.Rect(offset_x + x * CELL_SIZE, y * CELL_SIZE, offset_y + CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, WALL_COLOR, rect)