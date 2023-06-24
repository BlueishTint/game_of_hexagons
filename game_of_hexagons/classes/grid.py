def check_value(value: int):
    """Checks a value to make sure that it is valid and returns it

    :param int value: The value to check
    :raises ValueError: Raised if the value is not greater than 0
    :return int: Returns the value if it passes the check
    """
    if value < 1:
        raise ValueError("Value must be greater than 0")


class Grid:
    def __init__(self, x: int, y: int, default: int = 0):
        check_value(x)
        check_value(y)
        self._x = x
        self._y = y
        self._grid = [[default for _ in range(self.x)] for _ in range(self.y)]

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def grid(self):
        return self._grid

    def set_point(self, x: int, y: int, value: int):
        self._grid[x][y] = value

    def print_grid(self):
        for i, row in enumerate(self._grid):
            if i % 2:
                for n in row:
                    print(n, end=" ", flush=True)
                print()
            else:
                print("  ")
                for n in row:
                    print(n, end=" ", flush=True)
                print()

    def find_neighbors(self, x: int, y: int) -> list[tuple[int, int]]:
        top_cell = x, abs(len(self._grid) % (y + 1))  # up one cell
        bottom_cell = x, abs(len(self._grid) % (y - 1))  # down one cell
        top_left_cell = abs(len(self._grid) % (x - 1)), y  # one cell left
        top_right_cell = abs(len(self._grid) % (x + 1)), y  # one cell right
        bottom_left_cell = abs(len(self._grid) % (x - 1)), abs(
            len(self._grid) % (y - 1)
        )  # one cell down, one cell left
        bottom_right_cell = abs(len(self._grid) % (y + 1)), abs(
            len(self._grid) % (x - 1)
        )  # one cell down, one cell right
        return [
            top_cell,
            bottom_cell,
            top_right_cell,
            bottom_right_cell,
            bottom_left_cell,
            top_left_cell,
        ]

    def replace_neighbors(self, x: int, y: int):
        neighbors = self.find_neighbors(x, y)
        for neighbor in neighbors:
            self.set_point(neighbor[0], neighbor[1], 1)


my_grid = Grid(10, 10)

my_grid.set_point(5, 5, 8)

my_grid.replace_neighbors(5, 5)

my_grid.print_grid()
