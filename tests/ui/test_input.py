from snake_game_client.ui.ui_elements.input import Input

import pygame

pygame.init()

def test_input_initial_state():
    input_box = Input((100, 100, 200, 50), "Username")

    assert input_box.value == ""
    assert input_box.placeholder == "Username"
    assert input_box.active is False


def test_input_activate():
    input_box = Input((100, 100, 200, 50), "Username")

    event = pygame.event.Event(
        pygame.MOUSEBUTTONDOWN,
        {
            "button": 1,
            "pos": (150, 120)
        }
    )

    input_box.handle_event(event)

    assert input_box.active is True


def test_input_deactivate():
    input_box = Input((100, 100, 200, 50), "Username")

    input_box.active = True

    event = pygame.event.Event(
        pygame.MOUSEBUTTONDOWN,
        {
            "button": 1,
            "pos": (500, 500)
        }
    )

    input_box.handle_event(event)

    assert input_box.active is False


def test_input_typing():
    input_box = Input((100, 100, 200, 50), "Username")
    input_box.active = True

    event = pygame.event.Event(
        pygame.KEYDOWN,
        {
            "key": pygame.K_a,
            "unicode": "a"
        }
    )

    input_box.handle_event(event)

    assert input_box.value == "a"


def test_input_multiple_characters():
    input_box = Input((100, 100, 200, 50), "Username")
    input_box.active = True

    for character in "Janick":
        event = pygame.event.Event(
            pygame.KEYDOWN,
            {
                "key": ord(character.lower()),
                "unicode": character
            }
        )

        input_box.handle_event(event)

    assert input_box.value == "Janick"


def test_input_backspace():
    input_box = Input((100, 100, 200, 50), "Username")
    input_box.active = True
    input_box.value = "Hello"

    event = pygame.event.Event(
        pygame.KEYDOWN,
        {
            "key": pygame.K_BACKSPACE,
            "unicode": ""
        }
    )

    input_box.handle_event(event)

    assert input_box.value == "Hell"


def test_input_enter():
    input_box = Input((100, 100, 200, 50), "Username")
    input_box.active = True
    input_box.value = "Janick"

    event = pygame.event.Event(
        pygame.KEYDOWN,
        {
            "key": pygame.K_RETURN,
            "unicode": "\r"
        }
    )

    result = input_box.handle_event(event)

    assert result == "Janick"


def test_input_typing_when_inactive():
    input_box = Input((100, 100, 200, 50), "Username")

    event = pygame.event.Event(
        pygame.KEYDOWN,
        {
            "key": pygame.K_a,
            "unicode": "a"
        }
    )

    input_box.handle_event(event)

    assert input_box.value == ""