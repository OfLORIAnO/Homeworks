from typing import Union, TYPE_CHECKING

if TYPE_CHECKING:
    from board import Board


class Figure:
    x: int
    y: int
    board: "Board"

    def __init__(self, x: int, y: int, board: "Board"):
        super().__init__()
        self.x = x
        self.y = y

        self.board = board

    def getMoves(
        self,
    ) -> list[list[int]]:
        moves: list[Union[list[int], None]] = []
        x, y = self.x, self.y
        N: int = self.board.N

        # ? Ходы слона
        for index in range(1, N):
            moves.append(self.validate_move(x + index, y + index))
            moves.append(self.validate_move(x - index, y + index))
            moves.append(self.validate_move(x + index, y - index))
            moves.append(self.validate_move(x - index, y - index))

        # ? Ходы короля минус ходы слона
        moves.append(self.validate_move(x - 1, y))
        moves.append(self.validate_move(x + 1, y))
        moves.append(self.validate_move(x, y - 1))
        moves.append(self.validate_move(x, y + 1))

        filtered_moves: list[list[int]] = list(filter(None, moves))

        return filtered_moves

    def validate_move(self, x: int, y: int) -> Union[list, None]:
        if self.board.validate_position(x, y):
            return [x, y]
        return None
