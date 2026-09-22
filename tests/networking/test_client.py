from snake_game_client.networking.client import GameClient


def test_send_queues_message_without_connecting():
    client = GameClient("ws://example.invalid/ws")

    client.send({"type": "create_game"})

    assert client._outgoing.qsize() == 1
    assert client._outgoing.get() == {"type": "create_game"}


def test_incoming_starts_empty():
    client = GameClient("ws://example.invalid/ws")

    assert client.incoming.empty()
