from itertools import product
from typing import Tuple, List


def getMaxRoute(routes: list[list[int]]) -> list[int]:
    """
    Функция для нахождения наивыгодного маршрута

    Args:
    routes (List[List[int]]): Все входы в банки

    Returns:
    List[int]: Список с максимальной суммой денег и маршрутом банков
    """
    
    max: List[int] = routes[0]
    for i in range(1, len(routes)):
        elem: List[int] = routes[i]
        if max[0] <= elem[0]:
            max = elem
    return max


def banks() -> None:
    """
    Функция выводит наивыгодный маршрут
    Returns: None
    """

    banksList: List[Tuple[str, int]] = []

    n: int = int(input("Введите кол-во банков:"))
    for i in range(n):
        name: str = str(input("Введите название банка: "))
        money: int = int(input("Введите деньги банка: "))
        banksList.append((name, money))

    validMasks: List[str] = []
    for elem in product("01", repeat=len(banksList)):
        if "11" not in "".join(elem) and not "000" in "".join(elem):
            validMasks.append("".join(elem))

    vhodAfter: List[List] = []
    for i in range(len(validMasks)):
        mask = validMasks[i]
        totalSum: int = 0
        route: List[Tuple[str, int]] = []
        for j in range(len(mask)):
            if mask[j] == "1":
                totalSum += banksList[j][1]
                route.append((str(banksList[j][0]), int(j + 1)))
        vhodAfter.append([totalSum, route])
    print(getMaxRoute(vhodAfter))


if __name__ == "__main__":
    banks()
