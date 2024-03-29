from typing import Union, List, Tuple


def getMinDifferent() -> Union[Tuple[List[int], int], None]:
    """
    Функция для нахождения комбинации из 4 чисел в списке, которая ближе всего к заданной цели.

    Returns:
    - Union[Tuple[List[int], int], None]: Возвращает кортеж, содержащий найденную комбинацию и их сумму,
                                           либо None, если введено недостаточное количество элементов в списке.
    """

    # ? Список для хранения введенных чисел
    b: List[int] = []

    N: int = int(input("Введите количество элементов в списке(>4): "))
    if N < 4:
        return None
    for _ in range(N):
        b.append(int(input("Введите элемент списка: ")))

    C = int(input("Введите цель: "))
    
    if N == 4:
        return (b, C - sum(b))

    b.sort()

    metaData: Tuple[List[int], int] = (b[0:4], C - sum(b[0:4]))
    print(N, b, C)
    
    # ? 2 вложенных цикла + метод двух указателей - O(n^3)
    
    for i in range(N - 3):
        for j in range(i + 1, N - 2):
            first_sum: int = b[i] + b[j]
            left, right = j, N - 1

            while left < right:
                current_sum = b[left] + b[right] + first_sum
                (_, meta_sum) = metaData

                if abs(current_sum - C) < abs(meta_sum - C):
                    print(current_sum - C, meta_sum - C)
                    metaData = ([b[i], b[j], b[left], b[right]], current_sum)
                if current_sum < C:
                    left += 1
                else:
                    right -= 1

    return (metaData[0], C - metaData[1])


if __name__ == "__main__":
    print(getMinDifferent())
