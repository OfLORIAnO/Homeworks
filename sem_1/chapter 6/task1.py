elemsDict: dict[tuple, str] = {
    tuple([0, *range(4, 10)]): "элементов",
    (1,): "элемент",
    (2, 3): "элемента",
}


def getElemdict(n: int) -> str:
    """
    Возвращает слово "элемент" в нужной форме в зависимости от числа.

    Args:
    n: Число для определения формы слова "элемент".

    Return:
    str: Слово "элемент" в нужной форме.
    """

    for key, value in elemsDict.items():
        if n in key:
            return value
    else:
        return "элементов"


def getList(list_input: list[int]) -> str:
    """
    Возвращает строку с элементами списка, разделенными запятой.

    Args:
    list_input (List[int]): Список целых чисел.

    Return:
    str: Строка с элементами списка, разделенными запятой.
    """
    return ", ".join(list(map(str, list_input)))


def output_data(list1: list[int], list2: list[int]) -> None:
    """
    Выводит информацию о списках.

    Args:
    list1 (List[int]): Первый список чисел.
    list2 (List[int]): Второй список чисел.

    Return:
    None
    """

    set_li1 = set(list1)
    set_li2 = set(list2)

    notUnique_Data: list[int] = list(set_li1 & set_li2)
    notUnique_Data.sort()

    unique_data: list[int] = list(set_li1 ^ set_li2)
    unique_data.sort()

    l1_minus_l2 = list(set_li1 - set_li2)

    l2_minus_l1 = list(set_li2 - set_li1)

    print(
        f"1) {len(notUnique_Data)} {getElemdict(len(notUnique_Data))}: {getList(notUnique_Data)}"
    )
    print(
        f"2) {len(unique_data)} {getElemdict(len(unique_data))}: {getList(unique_data)}"
    )
    print(
        f"3) {len(l1_minus_l2)} {getElemdict(len(l1_minus_l2))}: {getList(l1_minus_l2)}"
    )
    print(
        f"4) {len(l2_minus_l1)} {getElemdict(len(l2_minus_l1))}: {getList(l2_minus_l1)}"
    )


if __name__ == "__main__":
    output_data(
        [0, 33, 37, 6, 10, 44, 13, 47, 16, 18, 22, 25],
        [1, 38, 48, 8, 41, 7, 12, 47, 16, 40, 20, 23, 25],
    )
