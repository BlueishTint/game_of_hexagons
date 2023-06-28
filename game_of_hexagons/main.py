import tkinter as tk
from random import randint
import time as t

from game_of_hexagons.classes import HexagonalGrid

HEIGHT = 800
WIDTH = 1300

root = tk.Tk()
root.title("awesomesauce grid")

canvas = tk.Canvas(master=root, bg="black", height=HEIGHT, width=WIDTH)

canvas.pack()

grid: HexagonalGrid = HexagonalGrid(100, 100)
grid.flip_points([(randint(0, 49), randint(0, 49)) for _ in range(1000)])
grid.create_hexagon_items(canvas, 10)
FILLED_HEXAGON_ITEM_IDS = canvas.find_withtag("filled")
EMPTY_HEXAGON_ITEM_IDS = canvas.find_withtag("empty")

def gameloop():
    grid.draw_grid(canvas, FILLED_HEXAGON_ITEM_IDS, EMPTY_HEXAGON_ITEM_IDS)
    grid.update()
    root.after(500, gameloop)


gameloop()
root.mainloop()
