from typing import Literal

# ? Imports helper module
from helper import get_evel, final_return, choose


# ? Types
num_arrType = list[str]
operaions_before_type = list[str]
operactionType = Literal["+", "-", "init", "end", "no solution"]


def output_data(list1: num_arrType) -> str:
    expression_equals: int = int(list1[len(list1) - 1])
    numArr, operationArr, operaction = recursion_func(file, [])
    if operaction == "no solution":
        return "no solution"
    return final_return(numArr, operationArr, str(expression_equals))


def recursion_func(
    num_arr: num_arrType,
    operaions_before: operaions_before_type = [],
    operation: operactionType = "init",
) -> tuple[num_arrType, operaions_before_type, operactionType]:
    expression_equals: int = int(num_arr[len(num_arr) - 1])

    # ? Первый заход в функцию
    if operation == "init":
        arr1, operaions_before1, operation1 = recursion_func(num_arr, ["+"], "+")
        arr2, operaions_before2, operation2 = recursion_func(num_arr, ["-"], "-")
        return choose(
            arr1, operaions_before1, operation1, arr2, operaions_before2, operation2
        )

    # ? Если Все знаки уже расставлены
    if len(operaions_before) == len(num_arr) - 2:
        # ? То, чему должно быть равно выражение
        totalAns = get_evel(num_arr, operaions_before)
        if (
            totalAns != False and expression_equals == totalAns
        ):  # ? Если выражение равно ожидаемому
            return (num_arr, operaions_before, "end")
        # ? Если выражение не равно ожидаемому, значит оно нам не подходит
        return ([], [], "no solution")

    # ? Продолжаем перебирать
    else:
        arr1, operaions_before1, operation1 = recursion_func(
            num_arr, operaions_before + ["+"], "+"
        )
        arr2, operaions_before2, operation2 = recursion_func(
            num_arr, operaions_before + ["-"], "-"
        )
        return choose(
            arr1, operaions_before1, operation1, arr2, operaions_before2, operation2
        )


if __name__ == "__main__":
    file: list[str] = open("lab1/nums.txt").readline().split()
    file = file[1 : len(file)]
    print(output_data(file))
