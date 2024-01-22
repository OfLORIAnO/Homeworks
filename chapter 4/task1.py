from itertools import combinations
from typing import Union, List, Tuple


def getMinDifferent() -> Union[Tuple[List[int], int], None]:
    """
    Функция для нахождения комбинации из 4 чисел в списке, которая ближе всего к заданной цели.

    Returns:
    - Union[Tuple[List[int], int], None]: Возвращает кортеж, содержащий найденную комбинацию и их сумму,
                                           либо None, если введено недостаточное количество элементов в списке.
    """

    # ? Количество элементов в комбинации
    lenSequence: int = 4

    # ? Список для хранения введенных чисел
    b: List[int] = []

    # ? Ввод количества элементов в списке
    N: int = int(input("Введите количество элементов в списке: "))

    # ? Ввод целочисленного списка
    for _ in range(N):
        b.append(int(input("Введите элемент списка: ")))

    # ? Ввод цели
    C = int(input("Введите цель: "))

    # ? Инициализация переменных для хранения минимальной суммы и соответствующей комбинации
    minList: List[int] = []
    minNum: float = float("-inf")

    # ? Перебираем все комбинации из lenSequence элементов
    for elem in combinations(b, lenSequence):
        # ? Если текущая комбинация ближе к цели, обновляем значения
        if abs(sum(elem) - C) < abs(minNum - C):
            minNum = sum(elem)
            minList = list(elem)

    # ? Возвращаем результат
    return minList, sum(minList)


if __name__ == "__main__":
    print(getMinDifferent())
