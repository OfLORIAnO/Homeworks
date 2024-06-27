from time import time
import copy
from numpy import array

from my_types import (
    symbol_type,
    board_type,
    solutions_type,
    total_solutions_type,
    init_positions_type,
)

# ? Константы
SYMBOL_FIGURE: symbol_type = [1, "#"]
SYMBOL_PERMISSIBLE: symbol_type = [2, "*"]
SYMBOL_EMPTY: symbol_type = [0, "0"]


class Solution:
    solutions_total: total_solutions_type

    def __init__(self, N: int, L: int, K: int, init_positions: init_positions_type):
        self.N = N
        self.L = L
        self.K = K
        self.solutions_total = []
        self.__main(init_positions)

    @classmethod
    def get_solutions(
        cls, N: int, L: int, K: int, init_positions: init_positions_type
    ) -> total_solutions_type:
        instance = cls(N, L, K, init_positions)
        return instance.solutions_total

    def __main(self, init_positions: init_positions_type) -> None:
        """
        Основная функция программы.

        Возвращает:
        - None
        """

        # ? Время начала работы
        init_time = time()

        # ? Инициализируем переменные
        solutions: solutions_type = []  # ? Решения на текущей итерации

        # ? Чтение входных данных из файла
        N = self.N
        K = self.K
        # ? Создаём доску и заполняем клетки пустотой
        board: board_type = array([[SYMBOL_EMPTY[0]] * self.N for _ in range(N)])

        # ? Добавляем существующие фигуры на доску
        for pos in init_positions:
            row, col = pos
            self.put_figure(board, N, row, col, solutions)

        print("Размер доски:", N, "Фигур стоит:", K, "Нужно разместить фигур:", self.L)

        # ? Если нужно поставить 0 фигур -> выходим
        if self.L == 0:
            if not (len(solutions) == 0):
                self.solutions_total.append(solutions)
            return self.__print_solutions(self.solutions_total, init_time)

        # ? Запускаем шарманку
        self.__print_board(board)
        self.__solve(board, 0, -1, self.L, N, solutions)

        # ? Выводим решения
        self.__print_solutions(self.solutions_total, init_time)

    @staticmethod
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

    def __put_inaccessible_passages(
        self, board: board_type, row: int, col: int, N: int
    ) -> None:
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
        for index in range(1, N):
            if flag1:
                flag1 = self.put_inaccessible(board, row + index, col + index, N)
            if flag2:
                flag2 = self.put_inaccessible(board, row - index, col + index, N)
            if flag3:
                flag3 = self.put_inaccessible(board, row + index, col - index, N)
            if flag4:
                flag4 = self.put_inaccessible(board, row - index, col - index, N)

        # ? Ходы короля минус ходы слона
        self.put_inaccessible(board, row - 1, col, N)
        self.put_inaccessible(board, row + 1, col, N)
        self.put_inaccessible(board, row, col - 1, N)
        self.put_inaccessible(board, row, col + 1, N)

    # ? Размещаем фигуры
    def put_figure(
        self, board: board_type, N: int, row: int, col: int, solutions: solutions_type
    ) -> None:
        """
        Размещает фигуру на доске и обновляет информацию о решении.

        Параметры:
        - board: Двумерный массив (доска), на которой производится размещение фигуры.
        - N: Размерность доски (количество строк и столбцов).
        - row: Номер строки клетки, на которой размещается фигура.
        - col: Номер столбца клетки, на которой размещается фигура.
        - solutions: Список расстановки в текущей ветке рекурсии.

        Возвращает:
        - None
        """

        board[row][col] = SYMBOL_FIGURE[0]
        solutions.append((row, col))
        self.__put_inaccessible_passages(board, row, col, N)

    def __solve(
        self,
        board: board_type,
        row: int,
        col: int,
        L: int,
        N: int,
        solutions: solutions_type,
    ) -> None:
        """
        Рекурсивно находит все возможные расстановки фигур на доске.
        Параметры:
        - board: Двумерный массив (доска), на которой производится размещение фигур.
        - row: Номер текущей строки на доске.
        - col: Номер текущего столбца на доске.
        - L: Количество оставшихся фигур для размещения.
        - N: Размерность доски (количество строк и столбцов).
        - solutions: Список расстановки в текущей ветке рекурсии.
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
            ):  # ? Если дошли до конца строки -> переходим на на следующую строку
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
                self.put_figure(current_board, N, row, col, current_solutions)
                # ?  Проверяем была ли эта фигура последней
                if L - 1 == 0:
                    self.solutions_total.append(current_solutions)
                    continue

                # ? Продолжаем крутить шарманку
                self.__solve(
                    current_board,
                    row,
                    col
                    + 1,  # ? Cледующая клетка не может быть доступной -> пропускаем её
                    L - 1,
                    N,
                    current_solutions,
                )

    # ? Вывод решений в файл
    @staticmethod
    def __print_solutions(solutions: total_solutions_type, init_time) -> None:
        """
        Выводит решения в файл, количество решений и время работы программы.

        Параметры:
        - solutions: Список расстановки в текущей ветке рекурсии.
        - init_time: Время начала выполнения программы.

        Возвращает:
        - None
        """

        # ? Вывод количества решений
        print("Количество решений:", len(solutions))
        # ? Вывод времени работы программы
        print("Время работы:", time() - init_time)

    # ? Вывод доски
    @staticmethod
    def __print_board(board: board_type) -> None:
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
