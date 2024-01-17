from typing import Union, Literal
from task1 import getLenOfNum


def reverseNum(num: int) -> Union[int, Literal["no solution"]]:
    """
    Реверсирует число, убирая ведущие нули, и возвращает результат.

    Args:
    - num (int): Целое число, которое требуется реверсировать.

    Returns:
    - Union[int, Literal["no solution"]]: Реверсированное число (если оно укладывается в диапазон [-128, 127]),
      либо строку "no solution", если реверсированное число выходит за пределы допустимого диапазона.

    """

    # ? Переменная для отслеживания отрицательности числа
    isNegative: bool = False

    # ? Если число отрицательное, сохраняем этот факт и работаем с модулем числа
    if num < 0:
        isNegative = True
        num = abs(num)

    # ? Переменная для хранения реверсированного числа
    newNum: int = 0

    # ? Цикл, который реверсирует число, убирая ведущие нули
    while num > 0:
        lastDigit: int = num % 10
        if lastDigit == 0:
            num //= 10
            continue
        newNum += 10 ** (getLenOfNum(num) - 1) * lastDigit
        num //= 10

    # ? Если изначальное число было отрицательным, возвращаем отрицательный результат
    if isNegative:
        newNum *= -1

    # ? Проверка, укладывается ли результат в допустимый диапазон [-128, 127]
    if not ((-(2**7)) <= newNum <= (2**7 - 1)):
        return "no solution"

    return newNum


if __name__ == "__main__":
    print("1", reverseNum(12))
    print("2", reverseNum(123))
    print("3", reverseNum(151))
    print("4", reverseNum(101))
    print("5", reverseNum(-110))
