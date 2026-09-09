import queue

from snake_game_client.ui.screens.game_screen import GameScreen


class FakeNetwork:
    def __init__(self):
        self.sent = []
        self.incoming = queue.Queue()

    def send(self, message):
        self.sent.append(message)


def test_game_screen_sends_create_game_on_init():
    network = FakeNetwork()

    GameScreen(None, lambda *a, **kw: None, 'classic', network)

    assert {"type": "create_game"} in network.sent


def test_send_direction_sends_expected_message():
    network = FakeNetwork()
    game_screen = GameScreen(None, lambda *a, **kw: None, 'classic', network)

    game_screen._send_direction((0, -1))

    assert network.sent[-1] == {"type": "set_direction", "direction": "up"}


def test_apply_server_state_infers_direction_from_movement():
    network = FakeNetwork()
    game_screen = GameScreen(None, lambda *a, **kw: None, 'classic', network)
    game_screen.snake.body = [(5, 5), (4, 5)]

    game_screen.apply_server_state([(5, 4), (5, 5)])

    assert game_screen.snake.direction == (0, -1)
    assert game_screen.snake.body == [(5, 4), (5, 5)]


def test_apply_server_state_keeps_direction_when_position_unchanged():
    network = FakeNetwork()
    game_screen = GameScreen(None, lambda *a, **kw: None, 'classic', network)
    game_screen.snake.direction = (1, 0)
    game_screen.snake.body = [(5, 5), (4, 5)]

    game_screen.apply_server_state([(5, 5), (4, 5)])

    assert game_screen.snake.direction == (1, 0)


def test_update_sets_game_over_flag_on_game_over_message():
    network = FakeNetwork()
    game_screen = GameScreen(None, lambda *a, **kw: None, 'classic', network)
    network.incoming.put({"type": "game_over", "game_id": "abc"})

    game_screen.update()

    assert game_screen.game_over is True
