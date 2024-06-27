from enum import Enum


class Color(Enum):
    white = "white"
    black = "black"
    green = "green"
    red = "red"
    yellow = "yellow"
    purple = "purple"


def get_color(color: Color) -> str:
    if color == Color.black:
        return "black"
    elif color == Color.white:
        return "white"
    elif color == Color.green:
        return "green"
    elif color == Color.red:
        return "red"
    elif color == Color.yellow:
        return "yellow"
    elif color == Color.purple:
        return "purple"
    return "white"
