import tkinter as tk
from random import randint

from game_of_hexagons.classes import HexagonalGrid

HEIGHT = 800
WIDTH = 1300

root = tk.Tk()
root.title("Awesomesauce Grid")

canvas = tk.Canvas(master=root, bg="black", height=HEIGHT, width=WIDTH)

canvas.pack()

grid: HexagonalGrid = HexagonalGrid(87, 47, 0, 1)

grid.flip_points([(randint(0, 86), randint(0, 46)) for _ in range(500)])
grid.create_hexagon_items(canvas, 10)
FILLED_HEXAGON_ITEM_IDS = canvas.find_withtag("filled")
EMPTY_HEXAGON_ITEM_IDS = canvas.find_withtag("empty")


def gameloop():
    grid.draw_grid(canvas, FILLED_HEXAGON_ITEM_IDS, EMPTY_HEXAGON_ITEM_IDS)
    grid.update()
    root.after(500, gameloop)


gameloop()
root.mainloop()
