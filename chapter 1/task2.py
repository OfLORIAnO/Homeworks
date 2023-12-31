from typing import Union, Literal
from task1 import getLenOfNum


def reverseNum(num: int) -> Union[int, Literal["no solution"]]:
    isNegative: bool = False
    if num < 0:
        isNegative = True
        num = abs(num)

    newNum: int = 0
    while num > 0:
        lastDigit: int = num % 10
        if lastDigit == 0:
            num //= 10
            continue
        newNum += 10 ** (getLenOfNum(num) - 1) * lastDigit
        num //= 10

    if isNegative:
        newNum *= -1
    if not ((-(2**7)) <= newNum <= (2**7 - 1)):
        return "no solution"

    return newNum


if __name__ == "__main__":
    print("1", reverseNum(12))
    print("2", reverseNum(123))
    print("3", reverseNum(151))
    print("4", reverseNum(101))
    print("5", reverseNum(-110))
