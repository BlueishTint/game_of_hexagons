from copy import deepcopy
from math import cos, radians
from tkinter import Canvas
from typing import Final, TypeVar, Generic

import numpy as np

T = TypeVar("T")
Coordinate = tuple[int, int]
COS30: Final = cos(radians(30))


def check_value(value: int):
    if value < 1:
        raise ValueError("Value must be greater than 0")


class Grid(Generic[T]):
    def __init__(self, width: int, height: int, off: T, on: T):
        self._width: Final = width
        self._height: Final = height
        self._off: Final = off
        self._on: Final = on
        self._grid = np.full((self.width, self.height), off)

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
        self.grid[coordinate[0], coordinate[1]] = value

    def flip_point(self, coordinate: Coordinate):
        if not self.is_coord_in_grid(coordinate):
            raise IndexError("That coordinate is not in the grid")
        if self.grid[coordinate[0], coordinate[1]] == self.on:
            self._set_point(coordinate, self.off)
        else:
            self._set_point(coordinate, self.on)

    def flip_points(self, coordinates: list[Coordinate]):
        for coordinate in coordinates:
            self.flip_point(coordinate)

    def print_grid(self):
        c = ""
        for column in range(self.height - 1):
            for row in range(self.width):
                c = f"{c} {self.grid[row, column]}"
                print(c)


class HexagonalGrid(Grid[T]):
    def __init__(self, width: int, height: int, off: T, on: T):
        super().__init__(width, height, off, on)

    def print_grid(self):
        for column in range(self.height - 1):
            c = ""
            if column % 2:
                c = f"{c} "
            for row in range(self.width):
                c = f"{c} {str(self.grid[row, column])}"
            print(c)

    def get_neighbors(self, coordinate: Coordinate) -> list[Coordinate]:
        top_cell = coordinate[0], (coordinate[1] + 1) % self.height  # up one cell
        bottom_cell = coordinate[0], (coordinate[1] - 1) % self.height  # down one cell
        top_left_cell = (coordinate[0] - 1) % self.width, coordinate[1]  # one cell left
        top_right_cell = (coordinate[0] + 1) % self.width, coordinate[
            1
        ]  # one cell right
        bottom_left_cell = (coordinate[0] - 1) % self.width, (
                (coordinate[1] - 1) % self.height
        ) % self.height  # one cell down, one cell left
        bottom_right_cell = (coordinate[0] + 1) % self.width, (
                (coordinate[1] - 1) % self.height
        ) % self.height  # one cell down, one cell right
        return [
            top_cell,
            bottom_cell,
            top_right_cell,
            bottom_right_cell,
            bottom_left_cell,
            top_left_cell,
        ]

    def update_point(self, coordinate: Coordinate, cached_grid: np.ndarray):
        neighbors = self.get_neighbors(coordinate)
        cells_on = 0

        for neighbor in neighbors:
            if cached_grid[neighbor[0], neighbor[1]] == 1:
                cells_on += 1

        if cells_on == 2 and cached_grid[coordinate[0], coordinate[1]] == self.off:
            self.flip_point(coordinate)
        elif (cells_on < 3 or cells_on > 4) and cached_grid[coordinate[0], coordinate[1]] == self.on:
            self.flip_point(coordinate)

    def update(self):
        cached_grid = deepcopy(self.grid)
        for x in range(self.width):
            for y in range(self.height):
                self.update_point((x, y), cached_grid)

    @staticmethod
    def create_hexagon(
            canvas: Canvas, radius: int, x: float, y: float, fill: str, tag: str = "hexagon"
    ):
        x1 = x - radius
        y1 = y
        x2 = x - radius / 2
        y2 = y + COS30 * radius
        x3 = x + radius / 2
        y3 = y2
        x4 = x + radius
        y4 = y
        x5 = x3
        y5 = y - COS30 * radius
        x6 = x2
        y6 = y5

        canvas.create_polygon(
            x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, outline="white", fill=fill, tags=tag
        )

    def draw_grid(self, canvas: Canvas, filled_hexagon_item_ids: tuple[int, ...],
                  empty_hexagon_item_ids: tuple[int, ...]):
        for x in range(self.width):
            for y in range(self.height):
                if self.grid[x, y] == self.off:
                    canvas.itemconfigure(filled_hexagon_item_ids[self.height * x + y], state="hidden")
                    canvas.itemconfigure(empty_hexagon_item_ids[self.height * x + y], state="normal")
                else:
                    canvas.itemconfigure(filled_hexagon_item_ids[self.height * x + y], state="normal")
                    canvas.itemconfigure(empty_hexagon_item_ids[self.height * x + y], state="hidden")

    def create_hexagon_items(self, canvas: Canvas, radius: int):
        x_scaling_factor = radius * 1.5
        y_scaling_factor = COS30 * radius * 2
        for x in range(0, self.width):
            for y in range(0, self.height):
                if x % 2 == 0:
                    yoffset = y_scaling_factor
                else:
                    yoffset = y_scaling_factor / 2
                self.create_hexagon(
                    canvas, radius, x_scaling_factor * x + radius, y_scaling_factor * y + yoffset,
                    "green", "filled"
                )
                self.create_hexagon(
                    canvas, radius, x_scaling_factor * x + radius, y_scaling_factor * y + yoffset,
                    "black", "empty"
                )
