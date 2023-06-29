import tkinter as tk
import argparse
from random import randint

from game_of_hexagons.classes import HexagonalGrid


def _parse_args() -> tuple[int, int, int]:
    parser = argparse.ArgumentParser(
        prog="Game of Hexagons",
        description="Conway's game of life with hexagons!",
    )
    parser.add_argument("--width", default=87, type=int)
    parser.add_argument("--height", default=47, type=int)
    parser.add_argument("--radius", default=10, type=int)

    args: dict[str, int] = vars(parser.parse_args())

    return (args["width"], args["height"], args["radius"])


def gameloop():
    grid.draw_grid(canvas, FILLED_HEXAGON_ITEM_IDS, EMPTY_HEXAGON_ITEM_IDS)
    grid.update()
    root.after(500, gameloop)


def main():
    gameloop()
    root.mainloop()


if __name__ == "__main__":
    WIDTH, HEIGHT, RADIUS = _parse_args()

    root = tk.Tk()
    root.title("Awesomesauce Grid")

    canvas = tk.Canvas(
        master=root,
        bg="black",
        width=int(WIDTH * RADIUS * 1.5),
        height=int(HEIGHT * RADIUS * 1.75),
    )

    canvas.pack()

    grid = HexagonalGrid(WIDTH, HEIGHT, 0, 1)

    grid.flip_points(
        [
            (randint(0, grid.width - 1), randint(0, grid.height - 1))
            for _ in range((WIDTH * HEIGHT) // 5)
        ]
    )
    grid.create_hexagon_items(canvas, RADIUS)
    FILLED_HEXAGON_ITEM_IDS = canvas.find_withtag("filled")
    EMPTY_HEXAGON_ITEM_IDS = canvas.find_withtag("empty")
    main()
