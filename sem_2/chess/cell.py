from typing import Union, TYPE_CHECKING

from color import Color
from utils import getCellColor, getStyleOfColor, Click_Type
from figure import Figure
from cell_button import Cell_button

if TYPE_CHECKING:
    from board import Board


class Cell:
    board: "Board"
    figure: Union[Figure, None]
    __is_available: bool
    __x: int
    __y: int
    color: Color
    button: Cell_button

    def __init__(self, x: int, y: int, board: "Board"):
        self.__x = x
        self.__y = y
        self.board = board
        self.__is_available = True
        self.figure = None

        self.button = Cell_button(self.on_click)

        self.Init()

    def Init(self):

        self.color = getStyleOfColor(getCellColor(self.__x, self.__y, self))
        self.button.setStyleSheet(self.get_color())
        self.render_symbol()

    def on_click(self, button_type: Click_Type):
        if button_type == Click_Type.left:
            self.put_figure()
        else:
            self.remove_figure()

        self.board.render()

    def render_symbol(self):
        if not (self.figure):
            self.button.setText("0")
            return
        self.button.setText("X")

    def render(self):
        newColor = getStyleOfColor(getCellColor(self.__x, self.__y, self))
        self.button.setStyleSheet(newColor)
        self.render_symbol()

    def get_color(self) -> Color:
        return self.color

    @property
    def is_available(self) -> bool:
        return self.__is_available

    @is_available.setter
    def is_available(self, state: bool = True):
        self.__is_available = state
        self.render()

    def put_figure(self):
        if not (self.__is_available) or self.figure:
            return
        else:
            self.figure = Figure(self.__x, self.__y, self.board)

    def remove_figure(self):
        self.figure = None
