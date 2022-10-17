import random
import tkinter
from typing import List
from tkinter import Button, Tk, DISABLED

class Cell:
    """Models each cell in a game of Minesweeper"""

    def __init__(self, x_coord, y_coord, cell_size, frame):
        self.size: int = cell_size
        self.hasBomb: bool = random.choices([True, False], cum_weights=(0.1, 0.9))[0]
        self.revealed: bool = False
        self.location = [x_coord, y_coord]
        self.frame = frame
        self.button = Button(frame, width=self.size, command=self.is_clicked)

    def announce_bomb(self):
        if self.hasBomb:
            return "T"
        else:
            return "F"

    def announce_location(self):
        return self.location

    def reveal(self):
        self.revealed = True
        print(f"{self.location} Revealed")
        self.button["state"] = DISABLED
        self.button["bg"] = "#bcbcbc"

    def is_clicked(self):
        self.reveal()


