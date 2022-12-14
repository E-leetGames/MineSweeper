import random
from typing import List


class Cell:

    """Models each cell in a game of Minesweeper"""

    def __init__(self, x_coord, y_coord, cell_size):
        self.size: int = cell_size
        self.hasBomb: bool = random.choices([True, False], cum_weights=(0.1, 0.9))[0]
        self.revealed: bool = False
        self.location: List[int] = [x_coord, y_coord]

    def announce_bomb(self):
        if self.hasBomb:
            return "T"
        else:
            return "F"

    def announce_location(self):
        return self.location

    def reveal(self):
        return True


