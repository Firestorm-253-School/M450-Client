import asyncio
import json
import queue
import threading

import websockets


class GameClient:
    def __init__(self, url: str):
        self._url = url
        self._outgoing: queue.Queue[dict] = queue.Queue()
        self.incoming: queue.Queue[dict] = queue.Queue()
        self._loop = asyncio.new_event_loop()
        self._thread = threading.Thread(target=self._run, daemon=True)

    def start(self) -> None:
        self._thread.start()

    def send(self, message: dict) -> None:
        self._outgoing.put(message)

    def _run(self) -> None:
        asyncio.set_event_loop(self._loop)
        self._loop.run_until_complete(self._connect())

    async def _connect(self) -> None:
        async with websockets.connect(self._url) as websocket:
            await asyncio.gather(
                self._send_loop(websocket),
                self._receive_loop(websocket),
            )

    async def _send_loop(self, websocket) -> None:
        while True:
            while not self._outgoing.empty():
                message = self._outgoing.get()
                await websocket.send(json.dumps(message))
            await asyncio.sleep(0.01)

    async def _receive_loop(self, websocket) -> None:
        async for raw_message in websocket:
            self.incoming.put(json.loads(raw_message))
