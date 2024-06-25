from PySide6.QtWidgets import (
    QPushButton,
    QPushButton,
)
from PySide6.QtCore import Qt
from color import Color
from utils import getCellColor, getStyleOfColor, Click_Type
from typing import Union
from figure import Figure


class Cell:
    board: "Board"
    figure: Union[Figure, None]
    is_available: bool
    x: int
    y: int
    color: Color
    button: QPushButton

    def __init__(self, x: int, y: int, board: "Board"):
        self.x = x
        self.y = y
        self.board = board
        self.is_available = True
        self.figure = None

        button = QPushButton()
        button.setFixedSize(64, 64)
        button.mousePressEvent = self.create_mouse_press_event()
        self.button = button

        self.Init()

    def Init(self):

        self.color = getStyleOfColor(getCellColor(self.x, self.y, self))
        self.button.setStyleSheet(self.get_color())
        self.render_symbol()

    def on_click(self, button_type: Click_Type):
        if button_type == Click_Type.left:
            self.put_figure(self.x, self.y)
        else:
            self.remove_figure()
        print(self.x + 1, self.y + 1)
        self.board.render()

    def create_mouse_press_event(self):
        def mousePressEvent(event):
            if event.button() == Qt.LeftButton:
                self.on_click(Click_Type.left)
            elif event.button() == Qt.RightButton:
                self.on_click(Click_Type.right)

        return mousePressEvent

    def render_symbol(self) -> str:
        if not (self.figure):
            self.button.setText("0")
            return
        self.button.setText("X")

    def render(self):
        newColor = getStyleOfColor(getCellColor(self.x, self.y, self))
        self.button.setStyleSheet(newColor)
        self.render_symbol()

    def get_color(self) -> Color:
        return self.color

    def set_available(self, state: bool = True):
        self.is_available = state
        self.render()

    def put_figure(self, x: int, y: int):
        if not (self.is_available):
            self.figure = None
        else:
            self.figure = Figure(self.x, self.y, self.board)

    def remove_figure(self):
        self.figure = None
