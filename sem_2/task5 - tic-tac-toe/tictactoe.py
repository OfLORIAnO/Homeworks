import random
from cell import Cell
from typing import Tuple


class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)

    __is_human_win: bool
    __is_computer_win: bool
    __is_draw: bool
    pole: Tuple[Tuple[Cell]]

    def __init__(self):
        self.init()

    def init(self):
        self.pole = tuple(tuple(Cell() for _ in range(3)) for __ in range(3))
        self.__is_human_win = False
        self.__is_computer_win = False
        self.__is_draw = False

    def show(self):
        for row in self.pole:
            print(" | ".join(str(cell.value) for cell in row))
        print()

    def human_go(self):
        while True:
            try:
                i, j = map(
                    int,
                    input("Enter row and column (0-2) separated by a space: ").split(),
                )
                if self.pole[i][j]:
                    self[i, j] = self.HUMAN_X
                    break
                else:
                    print("Cell is not free. Choose another one.")
            except (ValueError, IndexError):
                print(
                    "Invalid input. Please enter row and column numbers between 0 and 2."
                )

    def computer_go(self):
        while True:
            i, j = random.randint(0, 2), random.randint(0, 2)
            if self.pole[i][j]:
                self[i, j] = self.COMPUTER_O
                break

    @property
    def is_human_win(self):
        return self.__is_human_win

    @property
    def is_computer_win(self):
        return self.__is_computer_win

    @property
    def is_draw(self):
        return self.__is_draw

    def _check_winner(self):
        lines = (
            [
                [self.pole[i][0].value, self.pole[i][1].value, self.pole[i][2].value]
                for i in range(3)
            ]
            + [
                [self.pole[0][i].value, self.pole[1][i].value, self.pole[2][i].value]
                for i in range(3)
            ]
            + [
                [self.pole[0][0].value, self.pole[1][1].value, self.pole[2][2].value],
                [self.pole[0][2].value, self.pole[1][1].value, self.pole[2][0].value],
            ]
        )

        if [self.HUMAN_X] * 3 in lines:
            self.__is_human_win = True
        if [self.COMPUTER_O] * 3 in lines:
            self.__is_computer_win = True
        if (
            all(cell.value != self.FREE_CELL for row in self.pole for cell in row)
            and not self.__is_human_win
            and not self.__is_computer_win
        ):
            self.__is_draw = True

    def __getitem__(self, indices):
        i, j = indices
        if not (
            isinstance(i, int) and isinstance(j, int) and 0 <= i < 3 and 0 <= j < 3
        ):
            raise IndexError("некорректно указанные индексы")
        return self.pole[i][j].value

    def __setitem__(self, indices, value):
        i, j = indices
        if not (
            isinstance(i, int) and isinstance(j, int) and 0 <= i < 3 and 0 <= j < 3
        ):
            raise IndexError("некорректно указанные индексы")
        if value not in (self.FREE_CELL, self.HUMAN_X, self.COMPUTER_O):
            raise ValueError("некорректное значение")
        self.pole[i][j].value = value
        self._check_winner()

    def __bool__(self):
        return not (self.__is_human_win or self.__is_computer_win or self.__is_draw)
