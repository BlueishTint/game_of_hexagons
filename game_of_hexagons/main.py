import tkinter as tk
from random import randint

from game_of_hexagons.classes import HexagonalGrid

HEIGHT = 1000
WIDTH = 1000

root = tk.Tk()
root.title("awesomesauce grid")

canvas = tk.Canvas(master=root, bg="black", height=HEIGHT, width=WIDTH)

canvas.pack()

grid: HexagonalGrid = HexagonalGrid(100, 100)
grid.flip_points([(randint(0, 99), randint(0, 99)) for _ in range(1000)])


def gameloop():
    grid.draw_grid(canvas, 10)
    grid.update()
    root.after(500, gameloop)


gameloop()
root.mainloop()
