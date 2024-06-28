from typing import Union, TYPE_CHECKING

# Импортирование класса Board, если он доступен (для аннотаций типов)
if TYPE_CHECKING:
    from board import Board


# Класс фигуры
class Figure:
    x: int  # Координата X фигуры
    y: int  # Координата Y фигуры
    is_solution: bool  # Является ли фигура частью решения
    board: "Board"  # Ссылка на объект доски

    def __init__(self, x: int, y: int, board: "Board", is_solution: bool = False):
        super().__init__()
        self.x = x  # Установка координаты X
        self.y = y  # Установка координаты Y
        self.is_solution = is_solution  # Установка флага решения
        self.board = board  # Установка ссылки на доску

    def getMoves(self) -> list[list[int]]:
        # Получение возможных ходов фигуры
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
        # Проверка валидности хода
        if self.board._validate_position(
            x, y
        ):  # Проверка, находится ли позиция в пределах доски
            return [x, y]  # Возвращение валидной позиции
        return None  # Возвращение None для невалидной позиции
