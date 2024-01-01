from typing import Literal, Union, Any

# ? Imports helper module
from helper import get_evel, final_return


# ? Types
num_arrType = list[str]
operaions_before_type = list[str]
operactionType = Literal["+", "-", "init", "end", "no solution"]


def output_data(list1: num_arrType) -> str:
    expression_equals: int = int(list1[len(list1) - 1])
    numArr, operationArr, _ = recursion_func(file, [])
    return final_return(numArr, operationArr, str(expression_equals))


def recursion_func(
    num_arr: num_arrType,
    operaions_before: operaions_before_type = [],
    operation: operactionType = "init",
) -> tuple[num_arrType, operaions_before_type, operactionType]:
    expression_equals: int = int(num_arr[len(num_arr) - 1])
    if operation == "end":
        return num_arr, operaions_before, "end"
    # ? Первый заход в функцию
    if operation == "init":
        arr1, operaions_before1, operation1 = recursion_func(num_arr, ["+"], "+")
        arr2, operaions_before2, operation2 = recursion_func(num_arr, ["-"], "-")
        if operation1 == "end":
            return (arr1, operaions_before1, operation1)
        elif operation2 == "end":
            return (arr2, operaions_before2, operation2)
        else:
            return (arr2, operaions_before2, "no solution")

    # ? Если Все знаки уже расставлены
    if len(operaions_before) == len(num_arr) - 2:
        # ? То, чему должно быть равно выражение
        if get_evel(
            num_arr, operaions_before
        ) != False and expression_equals == get_evel(
            num_arr, operaions_before
        ):  # ? Если выражение равно ожидаемому
            return (num_arr, operaions_before, "end")
        # ? Если выражение не равно ожидаемому, значит оно нам не подходит
        else:
            return (num_arr, operaions_before, "no solution")

    # ? Продолжаем перебирать
    else:
        arr1, operaions_before1, operation1 = recursion_func(
            num_arr, operaions_before + ["+"], "+"
        )
        arr2, operaions_before2, operation2 = recursion_func(
            num_arr, operaions_before + ["-"], "-"
        )
        if operation1 == "end":
            return (arr1, operaions_before1, "end")
        elif operation2 == "end":
            return (arr2, operaions_before2, "end")
        else:
            return (["10"] * 10, [], "no solution")


if __name__ == "__main__":
    fileName: str = "nums.txt"
    path: str = f"lab1/{fileName}"

    file: list[str] = open(path).readline().split()

    print(output_data(file))
