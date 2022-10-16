

from cells import Cell
from tkinter import ttk, Frame


class Grd:
    def __init__(self, window_size, cell_size):
        self.size = (window_size // cell_size)
        self.grd = []
        self.cell_size = cell_size

    def make_grd(self):
        for i in range(self.size):
            for j in range(self.size):
                self.grd.append(Cell(i, j, self.cell_size))
        return self.grd

    def render(self, window, cell_size):
        grd_frame = Frame(window)

        for each in self.make_grd():
            button = ttk.Button(grd_frame, text=each.announce_bomb(), width=cell_size)
            button.grid(column=each.announce_location()[0], row=each.announce_location()[1])
        return grd_frame
