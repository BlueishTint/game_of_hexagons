# import tkinter as tk
from classes import *
from time import sleep

# First a function for creating hexagons, then tile
# then we would make an array or map of the grid
# update function

# grid = [[0 for _ in range(50)] for _ in range(50)]
# print(f"grid is {len(grid[0])}x{len(grid)}")

# root = tk.Tk()
# root.title("awesomesauce grid")

# canvas = tk.Canvas(master=root, bg="black", height=500, width=500)

# canvas.create_rectangle(100, 100, 200, 200, fill="white")

# canvas.pack()
# root.mainloop()

hexagonal_grid = HexagonalGrid(10, 10, 0, 1)
hexagonal_grid.flip_points([(3, 4), (4, 4)])

hexagonal_grid.print_grid()
while True:
    print("========================")
    hexagonal_grid.step_and_print()
    sleep(1)
