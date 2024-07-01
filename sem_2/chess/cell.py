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
    def __init__(self, x: int, y: int, board: "Board"):
        """
        Инициализация клетки на доске.

        Параметры:
        - x (int): Горизонтальная координата клетки на доске.
        - y (int): Вертикальная координата клетки на доске.
        - board (Board): Ссылка на объект доски, к которой принадлежит клетка.
        """
        self.__x: int = x
        self.__y: int = y
        self.board: "Board" = board
        self.__is_available: bool = True
        self.is_clickable: bool = True
        self.figure: Union[Figure, None] = None
        self.button: Cell_button = Cell_button(
            self.on_click
        )  # Инициализация кнопки с обработчиком кликов

        self.Init()  # Инициализация клетки

    def Init(self):
        """
        Инициализация цвета клетки и символа на кнопке.
        """
        self.__color = getStyleOfColor(getCellColor(self.__x, self.__y, self))
        self.button.setStyleSheet(self.__color)
        self.render_symbol()

    def on_click(self, button_type: Click_Type):
        """
        Обработчик кликов по кнопке клетки.

        Параметры:
        - button_type (Click_Type): Тип клика (левый или правый).
        """
        if button_type == Click_Type.left:
            self.put_figure()  # Левый клик - размещение фигуры
        else:
            self.remove_figure()  # Правый клик - удаление фигуры

        self.board.render()  # Перерисовка доски

    def render_symbol(self):
        """
        Отображение символа на кнопке в зависимости от наличия фигуры.
        """
        if not (self.figure):
            self.button.setText(" ")
        else:
            self.button.setText("X")

    def render(self):
        """
        Обновление цвета и символа на кнопке клетки.
        """
        newColor = getStyleOfColor(getCellColor(self.__x, self.__y, self))
        self.button.setStyleSheet(newColor)
        self.render_symbol()

    @property
    def is_available(self) -> bool:
        """
        Геттер для доступности клетки.

        Возвращаемое значение:
        - bool: True, если клетка доступна, False в противном случае.
        """
        return self.__is_available

    @is_available.setter
    def is_available(self, state: bool = True):
        """
        Сеттер для доступности клетки с перерисовкой.

        Параметры:
        - state (bool, optional): Состояние доступности клетки. По умолчанию True.
        """
        self.__is_available = state
        self.render()

    def put_figure(self, is_solution: bool = False):
        """
        Размещение фигуры на клетке.

        Параметры:
        - is_solution (bool, optional): Флаг указывающий, является ли размещение решением. По умолчанию False.
        """
        if not (self.is_clickable):
            Dialog("размещение фигур отключено", Color.red)
        elif not (self.__is_available) or self.figure:
            Dialog("нельзя поместить фигуру", Color.red)
        else:
            self.figure = Figure(self.__x, self.__y, self.board, is_solution)

    def remove_figure(self):
        """
        Удаление фигуры с клетки.
        """
        self.figure = None
