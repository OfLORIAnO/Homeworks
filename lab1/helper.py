# ? Импорт типов
from myTypes import (
    num_arr_type,
    operaions_before_type,
    operaction_type,
    recursion_return_type,
)


# ? Получение выражения
def get_expression(numArr: num_arr_type, operationArr: operaions_before_type):
    s: str = ""
    for i in range(len(operationArr)):
        s += numArr[i]
        s += operationArr[i]
    return s + numArr[i + 1]


# ? Вычисление выражения
def get_evel(numArr: num_arr_type, operationArr: operaions_before_type) -> int:
    return eval(get_expression(numArr, operationArr))


# ? Функция финального вывода
def final_return(
    numArr: num_arr_type,
    operationArr: operaions_before_type,
    operaction: operaction_type,
    expression_equals: str,
) -> str:
    if operaction == "no solution":
        return "no solution"
    return get_expression(numArr, operationArr) + "=" + expression_equals
    


# ? Функция выбора варианта
def choose(
    num_arr_1: num_arr_type,
    operaions_before_1: operaions_before_type,
    operation_1: operaction_type,
    num_arr_2: num_arr_type,
    operaions_before_2: operaions_before_type,
    operation_2: operaction_type,
) -> recursion_return_type:
    if operation_1 == "end":
        return (num_arr_1, operaions_before_1, "end")
    elif operation_2 == "end":
        return (num_arr_2, operaions_before_2, "end")
    return ([], [], "no solution")
