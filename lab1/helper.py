from typing import Union, Literal

from myTypes import num_arrType, operaions_before_type, operaction_type


def get_evel(numArr: list[str], operationArr: list[str]) -> Union[int, False]:
    try:
        s: str = ""
        for i in range(len(operationArr)):
            s += numArr[i]
            s += operationArr[i]
        s += numArr[i + 1]
        return eval(s)
    except:
        return False


def get_num(num: str) -> str:
    if int(num) < 0:
        return f" ({num}) "
    else:
        return num


def final_return(
    numArr: list[str],
    operationArr: list[str],
    operaction: operaction_type,
    expressionEquals: str,
) -> str:
    if operaction == "no solution":
        return "no solution"
    s: str = ""
    for i in range(len(operationArr)):
        s += get_num(numArr[i])
        s += f" {operationArr[i]} "
    s += get_num(numArr[i + 1]) + " = " + expressionEquals
    return s


def choose(
    num_arr_1: num_arrType,
    operaions_before_1: operaions_before_type,
    operation_1: operaction_type,
    num_arr_2: num_arrType,
    operaions_before_2: operaions_before_type,
    operation_2: operaction_type,
) -> tuple[num_arrType, operaions_before_type, operaction_type]:
    if operation_1 == "end":
        return (num_arr_1, operaions_before_1, "end")
    elif operation_2 == "end":
        return (num_arr_2, operaions_before_2, "end")
    return ([], [], "no solution")
