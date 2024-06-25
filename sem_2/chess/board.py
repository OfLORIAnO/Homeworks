from cell import Cell
from typing import Union

BoardType = list[list[Cell]]


class Board:
    N: int
    init_board: BoardType

    def __init__(self):
        self.Init()

    def Init(self):
        self.N = 8
        self.init_board = [[0 for x in range(self.N)] for y in range(self.N)]
        for x in range(self.N):
            for y in range(self.N):
                cell = Cell(x, y, self)
                self.init_board[x][y] = cell

    def get_cell(self, x: int, y: int) -> Union[Cell, None]:
        try:
            return self.init_board[x][y]
        except:
            print("мдээээ - выход за пределы доски")
            return None

    def reset_all_available(self):
        for x in range(self.N):
            for y in range(self.N):
                cell = self.get_cell(x, y)
                if cell:
                    cell.is_available = True

    def put_all_unavailable_cells(self):
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
                        unavailable_cell = self.get_cell(x, y)
                        if unavailable_cell:
                            unavailable_cell.is_available = False
                else:
                    cell.Init()

    def render_cells(self):
        N = self.N
        for x in range(N):
            for y in range(N):
                cell = self.get_cell(x, y)
                if cell:
                    cell.render()

    def render(self):
        self.reset_all_available()
        self.put_all_unavailable_cells()
        self.render_cells()

    def validate_position(self, x: int, y: int) -> bool:
        N: int = self.N
        return 0 <= x < N and 0 <= y < N

    def is_figure_on_cell(self, x: int, y: int) -> bool:
        cell = self.get_cell(x, y)
        if cell and cell.figure:
            return True
        return False
