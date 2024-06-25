from cell import Cell

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

    def get_cell(self, x: int, y: int) -> Cell:
        try:
            return self.init_board[x][y]
        except:
            print("мдээээ - выход за пределы доски")

    def check_cells_availability(self):
        N = self.N
        # ? проверяем все клетки
        for x in range(N):
            for y in range(N):
                cell: Cell = self.get_cell(x, y)
                # ? Если клетка занята, то рисуем ходы фигуры, стоящей на клетке
                if cell.figure:
                    moves = cell.figure.getMoves()
                    for move in moves:
                        [x, y] = move
                        unavailable_cell: Cell = self.get_cell(x, y)
                        if unavailable_cell:
                            unavailable_cell.set_available(False)
                else:
                    cell.Init()

    def render(self):
        N = self.N

        self.check_cells_availability()
        for x in range(N):
            for y in range(N):
                cell: Cell = self.get_cell(x, y)
                cell.render()

    def validate_position(self, x: int, y: int) -> bool:
        N: int = self.N
        return 0 <= x < N and 0 <= y < N
