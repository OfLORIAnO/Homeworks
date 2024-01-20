from typing import Any
from numpy import array
from time import time
import copy

# ? Импорт типов
from my_types import (
    symbol_type,
    board_type,
    solutions_type,
    total_solutions_type,
)

# ? Константы
SYMBOL_FIGURE: symbol_type = "#"
SYMBOL_PERMISSIBLE: symbol_type = "*"
SYMBOL_EMPTY: symbol_type = "0"


def put_inaccessible(board: board_type, row: int, col: int, N: int) -> bool:
    # ? Проверяем существует ли клетка
    if not (0 <= row < N and 0 <= col < N):
        # ? Проверяем не занята ли клетка
        return False
    if board[row][col] != SYMBOL_FIGURE:
        board[row][col] = SYMBOL_PERMISSIBLE
        return True
    return False


def put_inaccessible_passages(board: board_type, row: int, col: int, N: int) -> None:
    # ? Размещение недоступных клеток

    # ? Флаги нужны, чтоб не повторять выходы за пределы доски
    flag1, flag2, flag3, flag4 = True, True, True, True

    # ? Ходы слона
    for index in range(1, N - row):
        if flag1:
            flag1 = put_inaccessible(board, row + index, col + index, N)
        if flag2:
            flag2 = put_inaccessible(board, row - index, col + index, N)
        if flag3:
            flag3 = put_inaccessible(board, row + index, col - index, N)
        if flag4:
            flag4 = put_inaccessible(board, row - index, col - index, N)

    # ? Ходы короля минус ходы слона
    put_inaccessible(board, row - 1, col, N)
    put_inaccessible(board, row + 1, col, N)
    put_inaccessible(board, row, col - 1, N)
    put_inaccessible(board, row, col + 1, N)


# ? Размещаем фигуры
def put_figure(
    board: board_type, N: int, row: int, col: int, solutions: solutions_type
) -> None:
    board[row][col] = SYMBOL_FIGURE
    solutions.append((row, col))
    put_inaccessible_passages(board, row, col, N)


def solve(
    board: board_type,
    row: int,
    col: int,
    L: int,
    N: int,
    solutions: solutions_type,
    totalSolutions: total_solutions_type,
) -> None:
    # ? Рекурсивный алгоритм

    # ? Перебираем возможные ходы с текущей точки
    while True:
        col += 1

        if (
            col >= N
        ):  # ? Если дошли до конца строки -> переходимируем на следующую строку
            col = 0
            row += 1

        if row >= N:  # ? Если дошли до конца таблицы -> выходим
            break

        if board[row][col] == SYMBOL_EMPTY:  # ? Если клетка доступна для хода -> ходим
            # ? Пересоздаём данные в новые переменные
            current_board: board_type = array(board)
            current_solutions: solutions_type = copy.deepcopy(solutions)

            # ? Ставим фигуру
            put_figure(current_board, N, row, col, current_solutions)
            # ?  Проверяем была ли эта фигура последней
            if L - 1 == 0:
                totalSolutions.append(current_solutions)
                if len(totalSolutions) == 1:
                    print_board(current_board)
                continue

            # ? Размещаем фигуру
            solve(
                current_board,
                row,
                col + 1,  # ? Cледующая клетка не может быть доступной -> пропускаем её
                L - 1,
                N,
                current_solutions,
                totalSolutions,
            )


# ? Вывод решений в файл
def print_solutions(solutions: total_solutions_type, init_time) -> None:
    # ? Вывод решений в файл

    with open("lab2/output.txt", "w") as output_file:
        output_file.seek(0)  # ? Очищаем файл
        if not len(solutions):
            output_file.write("no solutions")
        else:
            for solution in solutions:
                output_file.write(" ".join([str(elem) for elem in solution]) + "\n")

    # ? Вывод количества решений
    print("Количество решений:", len(solutions))
    # ? Вывод времени работы программы
    print("Время работы:", time() - init_time)


def print_board(board: board_type) -> None:
    for row in board:
        print(" ".join(row))


# ? Основная функция
def main() -> None:
    # ? Время начала работы
    init_time = time()

    # ? Инициализируем переменные
    solutions: solutions_type = []  # ? Решения на текущей итерации
    totalSolutions: total_solutions_type = []  # ? Все решения

    # ? Чтение входных данных из файла
    with open("lab2/input.txt", "r") as input_file:
        N: int
        L: int
        K: int
        N, L, K = map(int, input_file.readline().split())

        # ? Создаём доску и заполняем клетки пустотой
        board: board_type = array([[SYMBOL_EMPTY] * N for _ in range(N)])

        # ? Добавляем существующие фигуры на доску
        for _ in range(K):
            row, col = map(int, input_file.readline().split())
            put_figure(board, N, row, col, solutions)
    print("Размер доски:", N, "Фигур стоит:", K, "Нужно разместить фигур:", L)

    # ? Если нужно поставить 0 фигур -> выходим
    if L == 0:
        return print_solutions(totalSolutions, init_time)

    # ? Запускаем шарманку
    solve(board, 0, 0, L, N, solutions, totalSolutions)

    # ? Выводим решения
    print_solutions(totalSolutions, init_time)


if __name__ == "__main__":
    main()
