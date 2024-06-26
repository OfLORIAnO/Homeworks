# Импорт необходимых классов и модулей
from cell import Cell
from typing import Union
from solution import Solution
from dialog import Dialog
from color import Color
from my_types import solutions_type, total_solutions_type
from PySide6.QtWidgets import (
    QGridLayout,  # Сетка для размещения виджетов
    QLineEdit,  # Текстовое поле ввода
)
from utils import get_number_from_input  # Утилита для получения числа из ввода
import random  # Для случайного выбора решений

# Типы для аннотаций
Board_type = list[list[Cell]]
Solutions_type = list[int]
Total_solutions_type = list[Solutions_type]


# Класс доски, наследующий QGridLayout
class Board(QGridLayout):
    N: int = 10  # Размер доски
    my_positions: solutions_type  # Позиции фигур, размещенных пользователем
    total_solutions: Total_solutions_type = list()  # Все возможные решения

    def __init__(
        self,
        init_positions: Union[solutions_type, None] = None,
        solution: Union[solutions_type, None] = None,
    ):
        super().__init__()
        self.__Init(init_positions, solution)

    def __Init(
        self,
        init_positions: Union[solutions_type, None] = None,
        solution: Union[solutions_type, None] = None,
    ):
        """Инициализация доски с начальными позициями и решением."""
        self.__Init__board()
        if init_positions is not None:
            self.__Init_start_Positions(init_positions)
        if solution is not None:
            self.__Init_solution_Positions(solution)
        self.render()
        self.__init_render_layout()

    def __Init_start_Positions(self, init_positions: solutions_type):
        """Установка начальных позиций фигур.

        Параметры:
        - init_positions (solutions_type): Список начальных позиций фигур на доске.
        """
        for position in init_positions:
            x, y = position
            cell = self.get_cell(x, y)
            if cell:
                cell.put_figure()

    def __Init_solution_Positions(self, solution: solutions_type):
        """Установка позиций для отображения решения.

        Параметры:
        - solution (solutions_type): Список позиций для отображения решения на доске.
        """
        for position in solution:
            x, y = position
            cell = self.get_cell(x, y)
            if cell:
                cell.put_figure(True)
        # Отключение возможности клика на клетках после отображения решения
        for x in range(self.N):
            for y in range(self.N):
                cell = self.get_cell(x, y)
                if cell:
                    cell.is_clickable = False

    def __Init__board(self):
        """Инициализация шахматной доски."""
        self.L = 2
        self.board = [[0 for _ in range(self.N)] for __ in range(self.N)]
        for x in range(self.N):
            for y in range(self.N):
                cell = Cell(x, y, self)
                self.board[x][y] = cell

    def __init_render_layout(self):
        """Инициализация и отрисовка раскладки доски."""
        for x in range(self.N):
            for y in range(self.N):
                cell = self.get_cell(x, y)
                if cell:
                    self.addWidget(cell.button, x, y)

    def get_cell(
        self, x: int, y: int, board: Union[Board_type, None] = None
    ) -> Union[Cell, None]:
        """Получение клетки по координатам.

        Параметры:
        - x (int): Координата по горизонтали.
        - y (int): Координата по вертикали.
        - board (Union[Board_type, None]): Доска, на которой производится поиск клетки.

        Возвращаемое значение:
        - Union[Cell, None]: Объект клетки (Cell) или None, если клетка не найдена.
        """
        current_board = board if board is not None else self.board
        try:
            return current_board[x][y]
        except:
            return None

    def render(self):
        """Полная отрисовка доски. Капитальная такая"""
        self.__reset_all_available()
        self.__put_all_unavailable_cells()
        self.__render_cells()

    def __reset_all_available(self):
        """Сброс доступности всех клеток."""
        for x in range(self.N):
            for y in range(self.N):
                cell = self.get_cell(x, y)
                if cell:
                    cell.is_available = True

    def __put_all_unavailable_cells(self):
        """Обновление состояния всех клеток."""
        N = self.N
        for x in range(N):
            for y in range(N):
                cell = self.get_cell(x, y)
                # Если клетка занята фигурой, обновляем ее ходы
                if cell and cell.figure:
                    moves = cell.figure.getMoves()
                    for move in moves:
                        move_x, move_y = move
                        move_cell = self.get_cell(move_x, move_y)
                        if move_cell:
                            move_cell.is_available = False
                else:
                    cell.Init()

    def __render_cells(self) -> None:
        """Отрисовка всех клеток."""
        N = self.N
        for x in range(N):
            for y in range(N):
                cell = self.get_cell(x, y)
                if cell:
                    cell.render()

    def _validate_position(self, x: int, y: int) -> bool:
        """Проверка валидности координат клетки.

        Параметры:
        - x (int): Координата по горизонтали.
        - y (int): Координата по вертикали.

        Возвращаемое значение:
        - bool: True, если координаты являются валидными для клетки на доске, False в противном случае.
        """
        N: int = self.N
        return 0 <= x < N and 0 <= y < N

    @staticmethod
    def pick_one_solution(solutions: total_solutions_type) -> solutions_type:
        """Выбор одного решения из списка решений.

        Параметры:
        - solutions (total_solutions_type): Список всех возможных решений.

        Возвращаемое значение:
        - solutions_type: Список позиций для отображения одного выбранного решения.
        """
        if len(solutions) == 0:
            return []
        positions_without_my = list()
        for positions in random.choice(solutions):
            if positions not in Board.my_positions:
                positions_without_my.append(positions)
        return positions_without_my

    def __put_my_positions(self):
        """Установка позиций фигур, размещенных пользователем."""
        my_positions = []
        for x in range(self.N):
            for y in range(self.N):
                cell = self.get_cell(x, y)
                if cell and cell.figure and not (cell.figure.is_solution):
                    my_positions.append((x, y))
        Board.my_positions = my_positions

    def __get_init_positions_for_solving(self):
        """Получение начальных позиций фигур для решения задачи.

        Возвращаемое значение:
        - solutions_type: Список начальных позиций фигур на доске.
        """
        init_positions = []
        for x in range(self.N):
            for y in range(self.N):
                cell = self.get_cell(x, y)
                if cell and cell.figure:
                    init_positions.append([x, y])
        return init_positions

    def start_solve(self):
        """Начало процесса решения задачи."""
        init_positions = self.__get_init_positions_for_solving()
        solutions = Solution.get_solutions(
            self.N, self.L, len(init_positions), init_positions
        )
        Board.total_solutions = solutions
        self.__put_my_positions()

    def change_L(self, L: str, input: QLineEdit):
        """Изменение значения L (количество фигур).

        Параметры:
        - L (str): Значение L, вводимое пользователем.
        - input (QLineEdit): Виджет текстового поля для ввода значения L.
        """
        newL = get_number_from_input(L)
        try:
            self.L = int(newL)
            input.setText(str(newL))
        except:
            self.L = 4
            input.setText(str(self.L))
            Dialog("некорректное значение L,\nL должно быть целым числом", Color.red)
