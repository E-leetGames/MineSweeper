# This is a clone of Minesweeper made to practice GUI and data structure basics.
from grd import Grd
from tkinter import ttk, Frame, Canvas, Tk, mainloop, Button, BOTTOM
from cells import Cell

window_size = 30
cell_size = 3
buttons = []


def setup():
    window = Tk()
    window.resizable(False, False)
    Grd.render(Grd(window_size, cell_size), window, cell_size).pack()
    exit_frame = Frame(window)
    exit_frame.pack(side=BOTTOM)
    exit_button = Button(exit_frame, text="EXIT", command=window.destroy)
    exit_button.pack()
    mainloop()


def get_button(bottom_frame, window):
    return Button(bottom_frame, text="EXIT", command=window.destroy)


setup()
