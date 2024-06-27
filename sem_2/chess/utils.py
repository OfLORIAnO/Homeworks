from enum import Enum
from color import Color
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from cell import Cell


class Click_Type(Enum):
    left = 0
    right = 1


text_styles = "font-size: 20px; font-weight: 700;"
border_styles = "border: none;"
cell_styles = text_styles + border_styles


def getStyleOfColor(color: Color) -> str:
    if color == Color.black:
        return "background-color: black; color: white;" + cell_styles
    elif color == Color.white:
        return "background-color: white; color: black;" + cell_styles
    elif color == Color.green:
        return "background-color: green; color: white;" + cell_styles
    elif color == Color.red:
        return "background-color: red; color: white;" + cell_styles
    elif color == Color.yellow:
        return "background-color: yellow; color: black;" + cell_styles
    elif color == Color.purple:
        return "background-color: purple; color: white;" + cell_styles

    return "background-color: white; color: black;" + cell_styles


def getInitCellColor(x: int, y: int) -> Color:
    if (x + y) % 2 == 0:
        return Color.white
    return Color.black


def getCellColor(x: int, y: int, cell: "Cell") -> Color:
    if cell.is_solution and not cell.figure:
        return Color.purple
    if cell.figure and cell.figure.is_solution:
        return Color.yellow
    if not (cell.is_available):
        return Color.red
    if not (cell.figure):
        return getInitCellColor(x, y)

    return Color.green


def get_number_from_input(text: str) -> str:
    newL = "0"
    if (len(text) == 0) or (text == " "):
        newL = "0"
    elif text and (text[0]) == "0" and len(text) > 1:
        newL = text[1:]
    else:
        newL = text
    return newL.strip()
