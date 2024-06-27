from enum import Enum
from color import Color
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from cell import Cell


class Click_Type(Enum):
    left = 0
    right = 1


text_styles = "font-size: 20px; font-weight: 700;"


def getStyleOfColor(color: Color) -> str:
    if color == Color.black:
        return "background-color: black; color: white;" + text_styles
    elif color == Color.white:
        return "background-color: white; color: black;" + text_styles
    elif color == Color.green:
        return "background-color: green; color: white;" + text_styles
    elif color == Color.red:
        return "background-color: red; color: white;" + text_styles
    elif color == Color.yellow:
        return "background-color: yellow; color: black;" + text_styles

    return "background-color: white; color: black;" + text_styles


def getInitCellColor(x: int, y: int) -> Color:
    if (x + y) % 2 == 0:
        return Color.white
    return Color.black


def getCellColor(x: int, y: int, cell: "Cell") -> Color:
    if cell.__is_solution:
        return Color.yellow
    if not (cell.is_available):
        return Color.red
    if not (cell.figure):
        return getInitCellColor(x, y)
    return Color.green
