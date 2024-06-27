from cell import Cell
from typing import Union
from solution import Solution
from dialog import Dialog
from color import Color
from typing import Union
from my_types import solutions_type, total_solutions_type
from PySide6.QtWidgets import (
    QGridLayout,
    QLineEdit,
)
from utils import get_number_from_input
import random

Board_type = list[list[Cell]]
Solutions_type = list[int]
Total_solutions_type = list[Solutions_type]


class Board(QGridLayout):
    N: int
    L: int
    total_solutions: Total_solutions_type = list()

    def __init__(
        self,
        init_positions: Union[solutions_type, None] = None,
        solution: Union[solutions_type, None] = None,
    ):
        super().__init__()
        self.Init(init_positions, solution)

    def Init(
        self,
        init_positions: Union[solutions_type, None] = None,
        solution: Union[solutions_type, None] = None,
    ):
        self.__Init__board()
        if init_positions is not None:
            self.__Init_start_Positions(init_positions)
        if solution is not None:
            self.__Init_solution_Positions(solution)
        self.render()
        self.init_render_layout()

    def __Init_start_Positions(self, init_positions: solutions_type):
        for position in init_positions:
            x, y = position
            cell = self.get_cell(x, y)
            if cell:
                cell.put_figure()

    def __Init_solution_Positions(self, solution: solutions_type):
        for position in solution:
            x, y = position
            cell = self.get_cell(x, y)
            if cell:
                cell.is_solution = True
                cell.put_figure(True)
        for x in range(self.N):
            for y in range(self.N):
                cell = self.get_cell(x, y)
                if cell:
                    cell.is_clickable = False

    def __Init__board(self):
        self.N = 10
        self.L = 2
        self.board = [[0 for _ in range(self.N)] for __ in range(self.N)]
        for x in range(self.N):
            for y in range(self.N):
                cell = Cell(x, y, self)
                self.board[x][y] = cell

    def get_cell(
        self, x: int, y: int, board: Union[Board_type, None] = None
    ) -> Union[Cell, None]:
        current_board = board
        if current_board is None:
            current_board = self.board
        try:
            return current_board[x][y]
        except:
            # Dialog(
            #     "Вообще не понимаю, как это могло произойти, но клетки не существует",
            #     Color.red,
            # )
            print("net")
            return None

    def __reset_all_available(self):
        for x in range(self.N):
            for y in range(self.N):
                cell = self.get_cell(x, y)
                if cell:
                    cell.is_available = True
                    cell.is_solution = False

    def __put_all_unavailable_cells(self):
        N = self.N
        # ? проверяем все клетки
        for x in range(N):
            for y in range(N):
                cell = self.get_cell(x, y)
                # ? Если клетка занята, то рисуем ходы фигуры, стоящей на клетке
                if cell and cell.figure:
                    moves = cell.figure.getMoves()
                    for move in moves:
                        [x, y] = move
                        move_cell = self.get_cell(x, y)
                        if move_cell:
                            if cell.figure.is_solution:
                                move_cell.is_available = False
                                move_cell.is_solution = True
                            else:
                                move_cell.is_solution = False
                                move_cell.is_available = False

                else:
                    cell.Init()

    def __render_cells(self) -> None:
        N = self.N
        for x in range(N):
            for y in range(N):
                cell = self.get_cell(x, y)
                if cell:
                    cell.render()

    def render(self):
        self.__reset_all_available()
        self.__put_all_unavailable_cells()
        self.__render_cells()

    def validate_position(self, x: int, y: int) -> bool:
        N: int = self.N
        return 0 <= x < N and 0 <= y < N

    def __get_init_positions__for_solving(self):
        init_positions = []
        for x in range(self.N):
            for y in range(self.N):
                cell = self.get_cell(x, y)
                if cell and cell.figure:
                    init_positions.append([x, y])
        return init_positions

    @staticmethod
    def pick_one_solution(solutions: total_solutions_type) -> solutions_type:
        if len(solutions) == 0:
            return []
        return random.choice(solutions)

    def start_solve(self):
        init_positions = self.__get_init_positions__for_solving()
        solutions = Solution.get_solutions(
            self.N, self.L, len(init_positions), init_positions
        )
        Board.total_solutions = solutions

        self.render()

    def change_L(self, L: str, input: QLineEdit):
        newL = get_number_from_input(L)
        try:
            self.L = int(newL)
            input.setText(str(newL))
        except:
            self.L = 4
            input.setText(str(self.L))
            Dialog("некорректное значение K,\nК должно быть целым числом", Color.red)

    def init_render_layout(self):
        for x in range(self.N):
            for y in range(self.N):
                cell = self.get_cell(x, y)
                if cell:
                    self.addWidget(cell.button, x, y)