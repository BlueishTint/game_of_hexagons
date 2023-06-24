import tkinter as tk
from classes import *
from time import sleep

# First a function for creating hexagons, then tile
# then we would make an array or map of the grid
# update function

# grid = [[0 for _ in range(50)] for _ in range(50)]
# print(f"grid is {len(grid[0])}x{len(grid)}")

root = tk.Tk()
root.title("awesomesauce grid")

canvas = tk.Canvas(master=root, bg="black", height=500, width=500)

def create_hexagon(radius: int, x: int, y: int):
    x1 = x - radius
    y1 = y
    x2 = x - radius/2
    y2 = y + 0.86602540378 * radius # 0.86602540378 = cos 30 degrees
    x3 = x + radius/2
    y3 = y2
    x4 = x + radius
    y4 = y
    x5 = x3
    y5 = y - 0.86602540378 * radius
    x6 = x2
    y6 = y5
    
    
    canvas.create_polygon(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, outline="green", fill="black")






canvas.pack()


hexagonal_grid = HexagonalGrid(20, 20, 0, 1)
hexagonal_grid.flip_points([(5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (8, 1), (7, 1)])

hexagonal_grid.print_grid()
while True:

    print("========================")
    hexagonal_grid.step_and_print()
    create_hexagon(10, 100, 100)
    root.mainloop()
    sleep(1)