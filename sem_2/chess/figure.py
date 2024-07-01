from typing import Union, TYPE_CHECKING

# Импортирование класса Board, если он доступен (для аннотаций типов)
if TYPE_CHECKING:
    from board import Board


# Класс фигуры
class Figure:
    def __init__(self, x: int, y: int, board: "Board", is_solution: bool = False):
        """
        Инициализация фигуры.

        Параметры:
        - x (int): Горизонтальная координата фигуры на доске.
        - y (int): Вертикальная координата фигуры на доске.
        - board (Board): Ссылка на объект доски, к которой принадлежит фигура.
        - is_solution (bool, optional): Флаг, указывающий, является ли фигура решением. По умолчанию False.
        """
        super().__init__()
        self.x = x  # Установка координаты X
        self.y = y  # Установка координаты Y
        self.is_solution = is_solution  # Установка флага решения
        self.board = board  # Установка ссылки на доску

    def getMoves(self) -> list[list[int]]:
        """
        Получение возможных ходов фигуры.

        Возвращаемое значение:
        - list[list[int]]: Список позиций, представляющих возможные ходы фигуры.
        """
        moves: list[Union[list[int], None]] = []
        x, y = self.x, self.y
        N: int = self.board.N  # Размер доски

        # Ходы слона (диагональные)
        for index in range(1, N):
            moves.append(
                self.validate_move(x + index, y + index)
            )  # Диагональ вправо-вниз
            moves.append(
                self.validate_move(x - index, y + index)
            )  # Диагональ влево-вниз
            moves.append(
                self.validate_move(x + index, y - index)
            )  # Диагональ вправо-вверх
            moves.append(
                self.validate_move(x - index, y - index)
            )  # Диагональ влево-вверх

        # Ходы короля (горизонтальные и вертикальные)
        moves.append(self.validate_move(x - 1, y))  # Влево
        moves.append(self.validate_move(x + 1, y))  # Вправо
        moves.append(self.validate_move(x, y - 1))  # Вверх
        moves.append(self.validate_move(x, y + 1))  # Вниз

        # Фильтрация валидных ходов
        filtered_moves: list[list[int]] = list(filter(None, moves))

        return filtered_moves

    def validate_move(self, x: int, y: int) -> Union[list[int], None]:
        """
        Проверка валидности хода для фигуры.

        Параметры:
        - x (int): Предполагаемая горизонтальная координата хода.
        - y (int): Предполагаемая вертикальная координата хода.

        Возвращаемое значение:
        - Union[list[int], None]: Список с координатами хода, если он валиден, или None, если ход невалиден.
        """
        if self.board._validate_position(
            x, y
        ):  # Проверка, находится ли позиция в пределах доски
            return [x, y]  # Возвращение валидной позиции
        return None  # Возвращение None для невалидной позиции
