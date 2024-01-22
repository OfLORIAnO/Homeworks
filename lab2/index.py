# ? Импорт пакетов
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
SYMBOL_FIGURE: symbol_type = [1, "#"]
SYMBOL_PERMISSIBLE: symbol_type = [2, "*"]
SYMBOL_EMPTY: symbol_type = [0, "0"]


def put_inaccessible(board: board_type, row: int, col: int, N: int) -> bool:
    """
    Помечает клетку на доске как недоступную для хода.

    Параметры:
    - board: Двумерный массив (доска), на которой производится маркировка клетки.
    - row: Номер строки клетки.
    - col: Номер столбца клетки.
    - N: Размерность доски (количество строк и столбцов).

    Возвращает:
    - bool: True, если клетка была успешно помечена, False в противном случае.
    """
    # ? Проверяем существует ли клетка
    if not (0 <= row < N and 0 <= col < N):
        # ? Проверяем не занята ли клетка
        return False
    if board[row][col] != SYMBOL_FIGURE[0]:  # ? Проверяем нет ли на клетке фигуры
        board[row][col] = SYMBOL_PERMISSIBLE[0]
        return True
    return False


def put_inaccessible_passages(board: board_type, row: int, col: int, N: int) -> None:
    """
    Размещает недоступные клетки на доске для ходов слона и короля.

    Параметры:
    - board: Двумерный массив (доска), на которой производится маркировка клеток.
    - row: Номер строки клетки.
    - col: Номер столбца клетки.
    - N: Размерность доски (количество строк и столбцов).

    Возвращает:
    - None
    """

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
    """
    Размещает фигуру на доске и обновляет информацию о решении.

    Параметры:
    - board: Двумерный массив (доска), на которой производится размещение фигуры.
    - N: Размерность доски (количество строк и столбцов).
    - row: Номер строки клетки, на которой размещается фигура.
    - col: Номер столбца клетки, на которой размещается фигура.
    - solutions: Список расстонов в текущей ветке рекурсии.

    Возвращает:
    - None
    """

    board[row][col] = SYMBOL_FIGURE[0]
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
    """
    Рекурсивно находит все возможные расстановки фигур на доске.

    Параметры:
    - board: Двумерный массив (доска), на которой производится размещение фигур.
    - row: Номер текущей строки на доске.
    - col: Номер текущего столбца на доске.
    - L: Количество оставшихся фигур для размещения.
    - N: Размерность доски (количество строк и столбцов).
    - solutions: Список расстонов в текущей ветке рекурсии.
    - totalSolutions: Список с общими решениями.

    Возвращает:
    - None
    """

    # ? Перебираем возможные ходы с текущей точки
    while True:
        # ? Идём на следующую клетку
        col += 1

        if (
            col >= N
        ):  # ? Если дошли до конца строки -> переходимируем на следующую строку
            col = 0
            row += 1

        if row >= N:  # ? Если дошли до конца таблицы -> выходим
            break

        if (
            board[row][col] == SYMBOL_EMPTY[0]
        ):  # ? Если клетка доступна для хода -> ходим
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

            # ? Продолжаем крутить шарманку
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
    """
    Выводит решения в файл, количество решений и время работы программы.

    Параметры:
    - solutions: Список расстонов в текущей ветке рекурсии.
    - init_time: Время начала выполнения программы.

    Возвращает:
    - None
    """

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


# ? Вывод доски
def print_board(board: board_type) -> None:
    """
    Выводит шахматную доску в консоль.

    Параметры:
    - board: Двумерный массив (доска), который нужно вывести.

    Возвращает:
    - None
    """
    for row in board:
        s: str = ""
        for elem in row:
            if elem == SYMBOL_FIGURE[0]:
                s += " " + SYMBOL_FIGURE[1]
            elif elem == SYMBOL_EMPTY[0]:
                s += " " + SYMBOL_EMPTY[1]
            else:  # ? Недоступная клетка
                s += " " + SYMBOL_PERMISSIBLE[1] 
        print(s)


# ? Основная функция
def main() -> None:
    """
    Основная функция программы.

    Возвращает:
    - None
    """

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
        board: board_type = array([[SYMBOL_EMPTY[0]] * N for _ in range(N)])

        # ? Добавляем существующие фигуры на доску
        for _ in range(K):
            row, col = map(int, input_file.readline().split())
            put_figure(board, N, row, col, solutions)

    print("Размер доски:", N, "Фигур стоит:", K, "Нужно разместить фигур:", L)

    # ? Если нужно поставить 0 фигур -> выходим
    if L == 0:
        if not (len(solutions) == 0):
            totalSolutions.append(solutions)
        print_board(board)
        return print_solutions(totalSolutions, init_time)

    # ? Запускаем шарманку
    solve(board, 0, -1, L, N, solutions, totalSolutions)

    # ? Выводим решения
    print_solutions(totalSolutions, init_time)


if __name__ == "__main__":
    main()
