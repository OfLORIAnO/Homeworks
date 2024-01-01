from itertools import combinations
from typing import Union


def getMinDifferent() -> Union[tuple[list[int], int], None]:
    lenSequence: int = 3
    b: list[int] = []

    N: int = int(input())
    if N < lenSequence:
        return None

    for _ in range(0, N):
        b.append(int(input()))
    C = int(input())

    minList: list[int] = []
    minNum: float = float("-inf")
    for elem in combinations(b, lenSequence):
        if abs(sum(elem) - C) < abs(minNum - C):
            minNum = sum(elem)
            minList = list(elem)

    return minList, sum(minList)


if __name__ == "__main__":
    print(getMinDifferent())
