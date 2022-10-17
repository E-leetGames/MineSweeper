# This is a clone of Minesweeper made to practice GUI and data structure basics.
from grd import Grd
from tkinter import ttk, Frame, Canvas, Tk, mainloop, Button, BOTTOM


window_size = 60
cell_size = 3
buttons = []
window = Tk()


def setup():
    window.resizable(False, False)
    Grd.render_grd(Grd(window_size, window, cell_size)).pack()
    exit_frame = Frame(window)
    exit_frame.pack(side=BOTTOM)
    exit_button = Button(exit_frame, text="EXIT", command=window.destroy)
    exit_button.pack()
    mainloop()


def re_render():
    Grd.render_grd(Grd(window_size, window, cell_size)).pack()


setup()
