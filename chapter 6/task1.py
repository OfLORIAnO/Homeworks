elemsDict: dict[tuple, str] = {
    tuple([0, *range(4, 10)]): "элементов",
    (1,): "элемент",
    (2, 3): "элемента",
}


def getElemdict(n: int) -> str:
    for key, value in elemsDict.items():
        if n in key:
            return value
    else:
        return "элементов"


def getList(list_input: list[int]) -> str:
    return ", ".join(list(map(str, list_input)))


def output_data(list1: list[int], list2: list[int]) -> None:
    notUnique_Data: list[int] = sorted([x for x in list1 if x in list2])

    unique_data: list[int] = sorted(
        [x for x in list1 if x not in list2] + [x for x in list2 if x not in list1]
    )

    l1_minus_l2 = list(set(list1) - set(list2))

    l2_minus_l1 = list(set(list2) - set(list1))

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
