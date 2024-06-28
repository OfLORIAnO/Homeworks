from typing import Callable, Union
from color import Color, get_color
from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Qt


# Класс диалогового окна
class Dialog(QDialog):
    __on_click: Union[Callable, None]  # Коллбэк для обработки кликов, или None

    def __init__(
        self, text: str, text_color: Color, on_click: Union[Callable, None] = None
    ):
        super().__init__()
        self.__on_click = on_click  # Установка коллбэка для кликов
        self.initUI(text, text_color)  # Инициализация интерфейса пользователя
        self.exec()  # Отображение диалогового окна

    def initUI(self, text: str, text_color: Color):
        # Инициализация пользовательского интерфейса
        self.setWindowTitle("Dialog")
        self.setFixedSize(300, 150)  # Установка фиксированного размера окна

        layout = QVBoxLayout()

        self.label = QLabel(text)  # Создание метки с текстом
        self.label.setAlignment(Qt.AlignCenter)  # Центрирование текста
        self.label.setStyleSheet(
            f"color: {get_color(text_color)};"
        )  # Установка цвета текста
        layout.addWidget(self.label)

        self.ok_button = QPushButton("OK")  # Создание кнопки OK
        self.ok_button.clicked.connect(
            self.__on_click_function
        )  # Привязка функции обработчика клика
        self.ok_button.clicked.connect(self.close)  # Привязка функции закрытия окна
        layout.addWidget(
            self.ok_button, alignment=Qt.AlignCenter
        )  # Добавление кнопки в макет

        self.setLayout(layout)  # Установка макета окна

    def __on_click_function(self):
        # Обработка клика по кнопке OK
        if self.__on_click:
            self.__on_click()  # Вызов коллбэка, если он установлен

        self.close()  # Закрытие диалогового окна
