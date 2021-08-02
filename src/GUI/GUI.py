import tkinter as tk
from GUI.Application import Application

WINDOW_NAME = " Get and Post"

window_size_height = 800
window_size_width = 700
GUI = None


def init(args):
    global GUI
    root = tk.Tk()
    root.resizable(False, False)
    set_window_size(root, window_size_height, window_size_width)
    center_window(root, window_size_height, window_size_width)
    GUI = Application(master=root)
    GUI.mainloop()


def set_window_size(window, window_height, window_width):
    window.geometry("%dx%d" % (window_width, window_height))


def center_window(window, window_height, window_width):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_coordinate = int((screen_width / 2) - (window_width / 2))
    y_coordinate = int((screen_height / 2) - (window_height / 2))
    window.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coordinate, y_coordinate))
