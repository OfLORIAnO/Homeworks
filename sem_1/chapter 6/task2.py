from typing import Any
from itertools import permutations


def getVariants(arr: list[Any]) -> None:
    """
    Выводит все возможные подмножества уникальных перестановок элементов списка.

    Args:
    arr (List[Any]): Список элементов.

    Return:
    None
    """
    s: list = list()
    for i in range(1, len(arr) + 1):
        for d in permutations(arr, i):
            if set(sorted(list(d))) not in s:
                s.append(set(list((d))))
    print("Подмножества:", s)
    print("Количество подмножеств:", len(s))


if __name__ == "__main__":
    getVariants(["a", "b", "c", "d", "d"])
