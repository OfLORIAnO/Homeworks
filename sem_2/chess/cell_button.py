from typing import Callable
from PySide6.QtWidgets import QPushButton
from PySide6.QtGui import QMouseEvent
from PySide6.QtCore import Qt

from utils import Click_Type


# Класс кнопки клетки
class Cell_button(QPushButton):

    def __init__(self, click_callback: Callable[[Click_Type], None]):
        """Инициализация кнопки клетки.

        Параметры:
        - click_callback (Callable[[Click_Type], None]): Функция обратного вызова, которая будет вызываться при клике на кнопку.
        """
        super().__init__()

        # Установка фиксированного размера кнопки
        self.setFixedSize(64, 64)
        self.click_callback = click_callback  # Установка коллбэка для кликов

    def mousePressEvent(self, event: QMouseEvent):
        """Обработка события нажатия кнопки мыши.

        Параметры:
        - event (QMouseEvent): Объект события нажатия кнопки мыши.
        """
        if event.button() == Qt.LeftButton:
            # Обработка левого клика мыши
            self.click_callback(Click_Type.left)
        elif event.button() == Qt.RightButton:
            # Обработка правого клика мыши
            self.click_callback(Click_Type.right)
