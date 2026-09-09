from dataclasses import dataclass


@dataclass
class Snake:
    body: list[tuple[int, int]]
    direction: tuple[int, int] = (1, 0)

    @classmethod
    def spawn_at(cls, position: tuple[int, int]) -> "Snake":
        direction = (1, 0)
        head_x, head_y = position
        tail = (head_x - direction[0], head_y - direction[1])
        return cls(body=[position, tail], direction=direction)

    def head(self) -> tuple[int, int]:
        return self.body[0]

    def move(self) -> None:
        head_x, head_y = self.head()
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)
        self.body = [new_head] + self.body[:-1]

    def grow(self) -> None:
        self.body.append(self.body[-1])

    def set_direction(self, direction: tuple[int, int]) -> None:
        opposite = (-self.direction[0], -self.direction[1])
        if direction != opposite:
            self.direction = direction

    def collides_with_self(self) -> bool:
        return self.head() in self.body[1:]
