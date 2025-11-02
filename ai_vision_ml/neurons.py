import os
import random
import sys
import time
from enum import Enum
from shutil import get_terminal_size


TICKS_PER_SECOND = 60


def clear() -> None:
    if sys.platform == "nt":
        os.system("cls")
    else:
        os.system("clear")


class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class Empty(str):
    CHAR = "  "

    def __new__(cls) -> str:
        return str.__new__(cls, cls.CHAR)


class Neuron(str):
    CHAR = "██"
    CHANCE_OF_DEATH = 35

    def __new__(cls) -> str:
        return str.__new__(cls, cls.CHAR)


class Grid:
    def __init__(self, width, height) -> None:
        self._grid = [[Empty() for _ in range(width)] for _ in range(height)]

    def __str__(self) -> str:
        return "\n".join(["".join(row) for row in self._grid])

    @property
    def neurons(self) -> tuple[tuple[Neuron, tuple[int, int]]]:
        return tuple(
            (element, (x, y))
            for y, row in enumerate(self._grid)
            for x, element in enumerate(row)
            if isinstance(element, Neuron)
        )

    def set_neuron(self, x, y) -> None:
        self._grid[y][x] = Neuron()

    def tick(self) -> None:
        for neuron_data in self.neurons:
            neuron = neuron_data[0]
            x, y = neuron_data[1]

            if random.randint(1, 100) <= Neuron.CHANCE_OF_DEATH:
                self._grid[y][x] = Empty()
                continue

            direction = random.choice(list(Direction))
            if direction == Direction.UP:
                y -= 1
            elif direction == Direction.RIGHT:
                x += 1
            elif direction == Direction.DOWN:
                y += 1
            elif direction == Direction.LEFT:
                x -= 1
            try:
                self._grid[y][x] = Neuron()
            except IndexError:
                pass


def main() -> None:
    width, height = get_terminal_size()
    grid = Grid(width // len(Neuron.CHAR), height)
    grid.set_neuron(15, 15) 
    grid.set_neuron(35, 35)
    while grid.neurons:
        clear()
        print(grid)
        grid.tick()
        time.sleep(1 / TICKS_PER_SECOND)


if __name__ == "__main__":
    while True:
        main()