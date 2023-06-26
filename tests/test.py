import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from game_of_hexagons.classes import *


def test_grid_creation():
    grid = HexagonalGrid(10, 10)
    assert grid.grid == [[0 for _ in range(10)] for _ in range(10)]


def test_flipping_point():
    grid = HexagonalGrid(10, 10)
    test_grid = [[0 for _ in range(10)] for _ in range(10)]
    test_grid[0][0] = 1
    grid.flip_point((0, 0))
    assert grid.grid == test_grid
