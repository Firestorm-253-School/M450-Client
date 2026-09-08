from snake_game_client.ui.button import Button 
import pygame
from unittest.mock import Mock


def test_button_hover(monkeypatch):
    button = Button(
        (100, 100, 200, 60),
        "Play",
        lambda: None,
        color=(100, 100, 100)
    )

    monkeypatch.setattr(
        pygame.mouse,
        "get_pos",
        lambda: (150, 120)
    )

    button.update()

    assert button.current_color == (80, 80, 80)


def test_button_no_hover(monkeypatch):
    button = Button(
        (100, 100, 200, 60),
        "Play",
        lambda: None,
        color=(100, 100, 100)
    )

    monkeypatch.setattr(
        pygame.mouse,
        "get_pos",
        lambda: (500, 500)
    )

    button.update()

    assert button.current_color == (100, 100, 100)


def test_button_click():
    on_click = Mock()

    button = Button(
        (100, 100, 200, 60),
        "Play",
        on_click
    )

    event = pygame.event.Event(
        pygame.MOUSEBUTTONDOWN,
        {
            "button": 1,
            "pos": (150, 120)
        }
    )

    button.handle_event(event)

    on_click.assert_called_once()


def test_button_click_outside():
    on_click = Mock()

    button = Button(
        (100, 100, 200, 60),
        "Play",
        on_click
    )

    event = pygame.event.Event(
        pygame.MOUSEBUTTONDOWN,
        {
            "button": 1,
            "pos": (500, 500)
        }
    )

    button.handle_event(event)

    on_click.assert_not_called()