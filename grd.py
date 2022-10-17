
from cells import Cell
from tkinter import ttk, Frame


class Grd:
    def __init__(self, window_size, window, cell_size):
        self.size = (window_size // cell_size)
        self.grd = []
        self.cell_size = cell_size
        self.grd_frame = Frame(window)
        self.make_grd()

    def make_grd(self):
        for i in range(self.size):
            for j in range(self.size):
                self.grd.append(Cell(i, j, self.cell_size, self.grd_frame))

    def render_grd(self):

        for each in self.grd:
            button = each.button
            button.grid(column=each.announce_location()[0], row=each.announce_location()[1])
        return self.grd_frame
