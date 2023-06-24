from typing import Final, TypeVar, Generic
from copy import deepcopy

T = TypeVar("T")
Coordinate = tuple[int, int]


def check_value(value: int):
    """Checks a value to make sure that it is valid and returns it

    :param int value: The value to check
    :raises ValueError: Raised if the value is not greater than 0
    :return int: Returns the value if it passes the check
    """
    if value < 1:
        raise ValueError("Value must be greater than 0")


class Grid(Generic[T]):
    def __init__(self, width: int, height: int, off: T = 0, on: T = 1):
        check_value(width)
        check_value(height)
        self._width: Final = width
        self._height: Final = height
        self._off: Final = off
        self._on: Final = on
        self._grid = [[off for _ in range(self.width)] for _ in range(self.height)]

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def grid(self):
        return self._grid

    @property
    def off(self):
        return self._off

    @property
    def on(self):
        return self._on

    def is_coord_in_grid(self, coordinate: Coordinate) -> bool:
        if coordinate[0] > self.width - 1 or coordinate[1] > self.height - 1:
            return False
        return True

    def _set_point(self, coordinate: Coordinate, value: T):
        self.grid[coordinate[1]][coordinate[0]] = value

    def flip_point(self, coordinate: Coordinate):
        if not self.is_coord_in_grid(coordinate):
            raise IndexError("That coordinate is not in the grid")
        if self.grid[coordinate[1]][coordinate[0]] == self.on:
            self._set_point(coordinate, self.off)
        else:
            self._set_point(coordinate, self.on)

    def flip_points(self, coordinates: list[Coordinate]):
        for coordinate in coordinates:
            self.flip_point(coordinate)

    def print_grid(self):
        for row in self.grid:
            print(row)


class HexagonalGrid(Grid[T]):
    def __init__(self, width: int, height: int, off: T = 0, on: T = 1):
        super().__init__(width, height, off, on)

    def print_grid(self):
        for i, row in enumerate(self.grid):
            if i % 2:
                for n in row:
                    print(n, end=" ", flush=True)
                print()
            else:
                print(end=" ")
                for n in row:
                    print(n, end=" ", flush=True)
                print()

    def get_neighbors(self, coordinate: Coordinate) -> list[Coordinate]:
        top_cell = coordinate[0], (coordinate[1] + 1) % self.height  # up one cell
        bottom_cell = coordinate[0], (coordinate[1] - 1) % self.height  # down one cell
        top_left_cell = (coordinate[0] - 1) % self.width, coordinate[1]  # one cell left
        top_right_cell = (coordinate[0] + 1) % self.width, coordinate[
            1
        ]  # one cell right
        bottom_left_cell = (coordinate[0] - 1) % self.width, (
            coordinate[1] - 1
        ) % self.height  # one cell down, one cell left
        bottom_right_cell = (coordinate[1] + 1) % self.width, (
            coordinate[0] - 1
        ) % self.height  # one cell down, one cell right
        return [
            top_cell,
            bottom_cell,
            top_right_cell,
            bottom_right_cell,
            bottom_left_cell,
            top_left_cell,
        ]

    def update_point(self, coordinate: Coordinate, cached_grid: list[list[T]]):
        neighbors = self.get_neighbors(coordinate)
        cells_on = 0

        for neighbor in neighbors:
            if cached_grid[neighbor[1]][neighbor[0]] == 1:
                cells_on += 1
        print(cells_on)

        if cells_on == 3 and cached_grid[coordinate[1]][coordinate[0]] == self.off:
            self.flip_point(coordinate)
        elif (cells_on < 2 or cells_on > 3) and cached_grid[coordinate[1]][
            coordinate[0]
        ] == self.on:
            self.flip_point(coordinate)

    def update(self):
        cached_grid = deepcopy(self.grid)
        for x in range(self.width):
            for y in range(self.height):
                self.update_point((x, y), cached_grid)

    def step_and_print(self):
        self.update()
        self.print_grid()


if __name__ == "__main__":
    from time import sleep

    my_grid = HexagonalGrid(10, 10)

    my_grid.flip_points([(4, 4), (5, 4), (4, 5)])
    print("======STARTING======")
    my_grid.print_grid()
    while True:
        print("========================")
        my_grid.step_and_print()
        sleep(1)
