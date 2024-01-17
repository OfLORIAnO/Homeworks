from copy import deepcopy
from typing import Tuple, Literal

# ? Типы
symbol_type = Literal["#", "*", "0"]

board_type = list[list[symbol_type]]

solutions_type = list[Tuple[int, int]]

total_solutions_type = list[solutions_type]

# ? Константы
symbol_figure: symbol_type = "#"
symbol_permissible: symbol_type = "*"
symbol_empty: symbol_type = "0"


def put_inaccessible_passages(board: board_type, row: int, col: int) -> None:
    # ? Размещение недоступных клеток

    # ? Ходы слона
    for index in range(len(board)):
        if (
            row < len(board)
            and row + index < len(board)
            and col + index < len(board)
            and board[row + index][col + index] != symbol_figure
        ):
            board[row + index][col + index] = symbol_permissible
        if (
            row < len(board)
            and col + index < len(board)
            and row - index >= 0
            and board[row - index][col + index] != symbol_figure
        ):
            board[row - index][col + index] = symbol_permissible
        if (
            col - index >= 0
            and row + index < len(board)
            and board[row + index][col - index] != symbol_figure
        ):
            board[row + index][col - index] = symbol_permissible
        if (
            row - index >= 0
            and col - index >= 0
            and board[row - index][col - index] != symbol_figure
        ):
            board[row - index][col - index] = symbol_permissible

    # ? Ходы Короля
    for i_row in range(row - 1, row + 2):
        for i_col in range(col - 1, col + 2):
            if i_row >= 0 and i_row < len(board) and i_col >= 0 and i_col < len(board):
                if board[i_row][i_col] != symbol_figure:
                    board[i_row][i_col] = symbol_permissible
    pass


def put_figure(
    board: board_type, row: int, col: int, solutions: solutions_type
) -> None:
    board[row][col] = symbol_figure
    solutions.append((row, col))
    put_inaccessible_passages(board, row, col)


def check_is_available(board: board_type, row: int, col: int) -> bool:
    return board[row][col] == symbol_empty


def solve(
    board: board_type,
    row: int,
    col: int,
    L: int,
    solutions: solutions_type,
    totalSolutions: total_solutions_type,
) -> None:
    # ? Рекурсивный алгоритм

    current_board: board_type = deepcopy(board)
    current_solutions: solutions_type = deepcopy(solutions)

    if check_is_available(current_board, row, col):
        put_figure(current_board, row, col, current_solutions)

    # ? Если расставили все фигуры
    if L == 0:
        print("---" * 7)
        print(current_board)
        totalSolutions.append(current_solutions)
        return

    cur_row: int = row
    cur_col: int = col

    while True:
        cur_col += 1
        if cur_col == len(board):
            cur_col = 0
            cur_row += 1

        if cur_row == len(board):
            break
        if check_is_available(current_board, cur_row, cur_col):
            solve(
                current_board,
                cur_row,
                cur_col,
                L - 1,
                current_solutions,
                totalSolutions,
            )


def print_solutions(solutions: total_solutions_type) -> None:
    # ? Вывод решений в файл
    with open("lab2/output.txt", "w") as output_file:
        output_file.seek(0)  # ? Очищаем файл
        if not len(solutions):
            output_file.write("no solutions")
        else:
            for solution in solutions:
                output_file.write(" ".join([str(elem) for elem in solution]) + "\n")


def main() -> None:
    # ? Чтение входных данных из файла
    with open("lab2/input.txt", "r") as input_file:
        N: int
        L: int
        K: int

        N, L, K = map(int, input_file.readline().split())

        # ? Добавляем существующие фигуры
        existing_figures: list[Tuple[int, int]] = []
        for _ in range(K):
            row, col = map(int, input_file.readline().split())
            existing_figures.append((row, col))

    # ? Создание доски и размещение уже существующих фигур
    board: board_type = [[symbol_empty] * N for _ in range(N)]
    solutions: solutions_type = []

    for figure in existing_figures:
        put_figure(board, figure[0], figure[1], solutions)

    # ? Решение
    totalSolutions: total_solutions_type = []
    solve(board, 0, 0, L, solutions, totalSolutions)
    print_solutions(totalSolutions)


if __name__ == "__main__":
    main()
