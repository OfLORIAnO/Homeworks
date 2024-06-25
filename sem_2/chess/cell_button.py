from typing import Callable
from PySide6.QtWidgets import QPushButton
from PySide6.QtGui import QMouseEvent
from PySide6.QtCore import Qt

from utils import Click_Type


class Cell_button(QPushButton):
    click_callback: Callable

    def __init__(self, click_callback: Callable[[Click_Type], None]):
        super().__init__()

        self.setFixedSize(64, 64)
        self.click_callback = click_callback

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.click_callback(Click_Type.left)
        elif event.button() == Qt.RightButton:
            self.click_callback(Click_Type.right)
