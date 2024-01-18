from typing import Any
from numpy import array
from time import time
import copy

# ? Импорт типов
from my_types import (
    existing_figures_type,
    symbol_type,
    board_type,
    solutions_type,
    total_solutions_type,
)

# ? Константы
SYMBOL_FIGURE: symbol_type = "#"
SYMBOL_PERMISSIBLE: symbol_type = "*"
SYMBOL_EMPTY: symbol_type = "0"


def put_inaccessible_passages(board: board_type, row: int, col: int) -> None:
    # ? Размещение недоступных клеток

    # ? Ходы слона
    for index in range(len(board)):
        if (
            row < len(board)
            and row + index < len(board)
            and col + index < len(board)
            and board[row + index][col + index] != SYMBOL_FIGURE
        ):
            board[row + index][col + index] = SYMBOL_PERMISSIBLE
        if (
            row < len(board)
            and col + index < len(board)
            and row - index >= 0
            and board[row - index][col + index] != SYMBOL_FIGURE
        ):
            board[row - index][col + index] = SYMBOL_PERMISSIBLE
        if (
            col - index >= 0
            and row + index < len(board)
            and board[row + index][col - index] != SYMBOL_FIGURE
        ):
            board[row + index][col - index] = SYMBOL_PERMISSIBLE
        if (
            row - index >= 0
            and col - index >= 0
            and board[row - index][col - index] != SYMBOL_FIGURE
        ):
            board[row - index][col - index] = SYMBOL_PERMISSIBLE

    # ? Ходы Короля
    for i_row in range(row - 1, row + 2):
        for i_col in range(col - 1, col + 2):
            if (
                i_row >= 0
                and i_row < len(board)
                and i_col >= 0
                and i_col < len(board)
                and board[i_row][i_col] != SYMBOL_FIGURE
            ):
                board[i_row][i_col] = SYMBOL_PERMISSIBLE


# ? Размещаем фигуры
def put_figure(
    board: board_type, row: int, col: int, solutions: solutions_type
) -> None:
    board[row][col] = SYMBOL_FIGURE
    solutions.append((row, col))
    put_inaccessible_passages(board, row, col)


# ? Проверка на доступность клетки
def check_is_available(board: board_type, row: int, col: int) -> bool:
    return board[row][col] == SYMBOL_EMPTY


def solve(
    board: board_type,
    row: int,
    col: int,
    L: int,
    solutions: solutions_type,
    totalSolutions: total_solutions_type,
) -> None:
    # ? Рекурсивный алгоритм

    # ? Если расставили все фигуры
    if L == 0:
        totalSolutions.append(solutions)
        return

    # ? Перебираем возможные ходы с текущей точки
    while True:
        col += 1
        if col == len(
            board
        ):  # ? Если дошли до конца строки -> переходимируем на следующую строку
            col = 0
            row += 1

        if row == len(board):  # ? Если дошли до конца таблицы -> выходим
            break

        if check_is_available(
            board, row, col
        ):  # ? Если клетка доступна для хода -> ходим
            # ? Пересоздаём данные в новые переменные
            current_board: Any = array(board)
            current_solutions: solutions_type = copy.deepcopy(solutions)

            # ? Размещаем фигуру
            put_figure(current_board, row, col, current_solutions)
            solve(
                current_board,
                row,
                col,
                L - 1,
                current_solutions,
                totalSolutions,
            )


def print_solutions(solutions: total_solutions_type, t1) -> None:
    # ? Вывод решений в файл
    with open("lab2/output.txt", "w") as output_file:
        output_file.seek(0)  # ? Очищаем файл
        if not len(solutions):
            output_file.write("no solutions")
        else:
            for solution in solutions:
                output_file.write(" ".join([str(elem) for elem in solution]) + "\n")
    print(time() - t1)
    print(len(solutions))


def main() -> None:
    t1 = time()
    # ? Чтение входных данных из файла
    with open("lab2/input.txt", "r") as input_file:
        N: int
        L: int
        K: int

        N, L, K = map(int, input_file.readline().split())

        # ? Добавляем существующие фигуры
        existing_figures: existing_figures_type = []
        for _ in range(K):
            row, col = map(int, input_file.readline().split())
            existing_figures.append((row, col))

    # ? Создание доски и размещение уже существующих фигур
    board: board_type = array([[SYMBOL_EMPTY] * N for _ in range(N)])

    # ? Создаём список решений
    solutions: solutions_type = []
    totalSolutions: total_solutions_type = []

    for figure in existing_figures:
        put_figure(board, figure[0], figure[1], solutions)

    # ? Решение
    solve(board, 0, 0, L, solutions, totalSolutions)
    print_solutions(totalSolutions, t1)


if __name__ == "__main__":
    main()
