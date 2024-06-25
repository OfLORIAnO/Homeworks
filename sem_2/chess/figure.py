class Figure:
    x: int
    y: int
    board: "Board"

    def __init__(self, x: int, y: int, board: "Board"):
        self.x = x
        self.y = y
        self.board = board

    def getMoves(
        self,
    ) -> list[list[int]]:
        moves = []
        x, y = self.x, self.y
        N: int = self.board.N

        # ? Ходы слона
        for index in range(1, N - x):
            moves.append(self.validate_move(x + index, y + index))
            moves.append(self.validate_move(x - index, y + index))
            moves.append(self.validate_move(x + index, y - index))
            moves.append(self.validate_move(x - index, y - index))

        # ? Ходы короля минус ходы слона
        moves.append(self.validate_move(x - 1, y))
        moves.append(self.validate_move(x + 1, y))
        moves.append(self.validate_move(x, y - 1))
        moves.append(self.validate_move(x, y + 1))

        return filter(None, moves)

    def validate_move(self, x: int, y: int):
        if not (self.board.validate_position(x, y)):
            return False
        try:
            cell = self.board.get_cell(x, y)
            if cell and cell.figure:
                return False
            return [x, y]
        except:
            return False
