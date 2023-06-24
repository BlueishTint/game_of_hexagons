import tkinter as tk

# First a function for creating hexagons, then tile
# then we would make an array or map of the grid
# update function

grid = [[0 for _ in range(50)] for _ in range(50)]
print(f"grid is {len(grid[0])}x{len(grid)}")

root = tk.Tk()
root.title("awesomesauce grid")

canvas = tk.Canvas(master=root, bg="black", height=500, width=500)

canvas.create_rectangle(100, 100, 200, 200, fill="white")

canvas.pack()
root.mainloop()


def find_neighbors_hexagon(grid: list[list[int]], x: int, y: int) -> list[int]:
    top_cell = grid[x][abs(len(grid) % (y + 1))]  # up one cell
    bottom_cell = grid[x][abs(len(grid) % (y - 1))]  # down one cell
    top_left_cell = grid[abs(len(grid) % (x - 1))][y]  # one cell left
    top_right_cell = grid[abs(len(grid) % (x + 1))][y]  # one cell right
    bottom_left_cell = grid[abs(len(grid) % (x - 1))][
        abs(len(grid) % (y - 1))
    ]  # one cell down, one cell left
    bottom_right_cell = grid[abs(len(grid) % (x + 1))][
        abs(len(grid) % (y - 1))
    ]  # one cell down, one cell right
    return [
        top_cell,
        bottom_cell,
        top_right_cell,
        bottom_right_cell,
        bottom_left_cell,
        top_left_cell,
    ]


def update_hexagon(
    self: int,
    top: int,
    bottom: int,
    top_left: int,
    bottom_left: int,
    top_right: int,
    bottom_right: int,
):
    cells_on = top + bottom + top_left + bottom_left + top_right + bottom_right

    if not self and cells_on == 3:
        return 1

    if cells_on == 4:
        return 1
    return 0
