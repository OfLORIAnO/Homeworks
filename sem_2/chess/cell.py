# Импорт необходимых классов и модулей
from typing import Union, TYPE_CHECKING
from color import Color
from utils import getCellColor, getStyleOfColor, Click_Type
from figure import Figure
from cell_button import Cell_button
from dialog import Dialog

# Импортирование класса Board, если он доступен (для аннотаций типов)
if TYPE_CHECKING:
    from board import Board


# Класс клетки доски
class Cell:
    board: "Board"  # Ссылка на объект доски
    figure: Union[Figure, None]  # Фигура, расположенная на клетке, или None
    __is_available: bool  # Доступность клетки для размещения фигуры
    __x: int  # Координата X клетки
    __y: int  # Координата Y клетки
    __color: Color  # Цвет клетки
    is_clickable: bool  # Возможность клика по клетке
    button: Cell_button  # Кнопка, связанная с клеткой

    def __init__(self, x: int, y: int, board: "Board"):
        self.__x = x
        self.__y = y
        self.board = board
        self.__is_available = True
        self.is_clickable = True
        self.figure = None
        self.button = Cell_button(
            self.on_click
        )  # Инициализация кнопки с обработчиком кликов

        self.Init()  # Инициализация клетки

    def Init(self):
        # Инициализация цвета клетки и символа на кнопке
        self.__color = getStyleOfColor(getCellColor(self.__x, self.__y, self))
        self.button.setStyleSheet(self.__color)
        self._render_symbol()

    def on_click(self, button_type: Click_Type):
        # Обработчик кликов по кнопке
        if button_type == Click_Type.left:
            self.put_figure()  # Левый клик - размещение фигуры
        else:
            self.remove_figure()  # Правый клик - удаление фигуры

        self.board._render()  # Перерисовка доски

    def _render_symbol(self):
        # Отображение символа на кнопке в зависимости от наличия фигуры
        if not (self.figure):
            self.button.setText(" ")
        else:
            self.button.setText("X")

    def _render(self):
        # Обновление цвета и символа на кнопке
        newColor = getStyleOfColor(getCellColor(self.__x, self.__y, self))
        self.button.setStyleSheet(newColor)
        self._render_symbol()

    @property
    def is_available(self) -> bool:
        # Геттер для доступности клетки
        return self.__is_available

    @is_available.setter
    def is_available(self, state: bool = True):
        # Сеттер для доступности клетки с перерисовкой
        self.__is_available = state
        self._render()

    def put_figure(self, is_solution: bool = False):
        # Размещение фигуры на клетке
        if not (self.is_clickable):
            Dialog("размещение фигур отключено", Color.red)
        elif not (self.__is_available) or self.figure:
            Dialog("нельзя поместить фигуру", Color.red)
        else:
            self.figure = Figure(self.__x, self.__y, self.board, is_solution)

    def remove_figure(self):
        # Удаление фигуры с клетки
        self.figure = None
