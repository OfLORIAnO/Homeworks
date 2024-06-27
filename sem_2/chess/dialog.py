from typing import Callable, Union
from color import Color, get_color
from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Qt


class Dialog(QDialog):
    __on_click: Union[Callable, None]

    def __init__(
        self, text: str, text_color: Color, on_click: Union[Callable, None] = None
    ):
        super().__init__()
        self.initUI(text, text_color)
        self.__on_click = on_click
        self.exec()

    def initUI(self, text: str, text_color: Color):
        self.setWindowTitle("Dialog")
        self.setFixedSize(300, 150)

        layout = QVBoxLayout()

        self.label = QLabel(text)
        self.label.setAlignment(Qt.AlignCenter)

        # Установка цвета текста
        self.label.setStyleSheet(f"color: {get_color(text_color)};")
        layout.addWidget(self.label)

        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.__on_click_function)
        self.ok_button.clicked.connect(self.close)
        layout.addWidget(self.ok_button, alignment=Qt.AlignCenter)

        self.setLayout(layout)

    def __on_click_function(self):
        if self.__on_click:
            self.__on_click()

        self.close()
