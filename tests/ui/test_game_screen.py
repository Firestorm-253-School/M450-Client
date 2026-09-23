import queue
from unittest.mock import Mock

from snake_game_client.game.player import PlayerData
from snake_game_client.ui.screens.game_screen import GameScreen


class FakeNetwork:
    def __init__(self):
        self.sent = []
        self.incoming = queue.Queue()

    def send(self, message):
        self.sent.append(message)


def _make_game(username="player1"):
    game = Mock()
    game.player.username = username
    return game


def _make_game_screen(network=None, map_name="classic", game_id="abc", game=None):
    if network is None:
        network = FakeNetwork()
    if game is None:
        game = _make_game()
    return GameScreen(
        None,
        game,
        {"map": map_name, "game_id": game_id},
        network,
    ), network, game


def test_game_screen_sets_map_and_game_id_on_init():
    game_screen, _, _ = _make_game_screen(map_name="medium", game_id="game-42")

    assert game_screen.map_name == "medium"
    assert game_screen.game_id == "game-42"


def test_send_direction_sends_expected_message():
    game_screen, network, _ = _make_game_screen()

    game_screen._send_direction((0, -1))

    assert network.sent[-1] == {"type": "set_direction", "direction": "up"}


def test_apply_server_state_updates_snake_from_player_data():
    game_screen, _, _ = _make_game_screen()
    players = {
        "player1": PlayerData(
            body=[(5, 4), (5, 5)],
            alive=True,
            direction=(0, -1),
        )
    }

    game_screen.apply_server_state(players, [])

    assert game_screen.snakes["player1"].direction == (0, -1)
    assert game_screen.snakes["player1"].body == [(5, 4), (5, 5)]


def test_apply_server_state_sets_game_over_when_local_player_dies():
    game_screen, _, _ = _make_game_screen()
    players = {
        "player1": PlayerData(
            body=[(5, 5), (4, 5)],
            alive=False,
            direction=(1, 0),
        )
    }

    game_screen.apply_server_state(players, [])

    assert game_screen.game_over is True


def test_update_sets_game_over_flag_on_game_over_message():
    game_screen, network, _ = _make_game_screen()
    game_screen.ui_elements = set()
    network.incoming.put({"type": "game_over", "game_id": "abc"})

    game_screen.update()

    assert game_screen.game_over is True


def test_bite_sound_plays_when_apple_is_eaten():
    game_screen, network, game = _make_game_screen()
    game_screen.ui_elements = set()
    game_screen.apples = [(5, 5), (10, 10)]

    network.incoming.put({
        "type": "game_state",
        "apples": [[5, 5]],
        "snakes": {
            "player1": {
                "snake": [[1, 1]],
                "alive": True,
                "direction": [1, 0],
            }
        },
    })

    game_screen.update()

    game.sound_bite.play.assert_called_once()


def test_apply_apples_from_game_state():
    game_screen, network, _ = _make_game_screen()
    game_screen.ui_elements = set()

    network.incoming.put({
        "type": "game_state",
        "apples": [[5, 5], [3, 3]],
        "snakes": {
            "player1": {
                "snake": [[1, 1]],
                "alive": True,
                "direction": [1, 0],
            }
        },
    })

    game_screen.update()

    assert len(game_screen.apples) == 2
    assert game_screen.apples == [(5, 5), (3, 3)]
