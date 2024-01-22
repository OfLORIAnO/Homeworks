# ? Импорт типов
from my_types import (
    num_arr_type,
    operations_before_type,
    operaction_type,
    recursion_return_type,
)


# ? Получение выражения
def get_expression(numArr: num_arr_type, operationArr: operations_before_type):
    """
    Получает выражение на основе списка чисел и списка операций.

    Parameters:
    - numArr (List[str]): Список чисел.
    - operationArr (List[str]): Список операций.

    Returns:
    - str: Полученное выражение.
    """
    s: str = ""
    for i in range(len(operationArr)):
        s += numArr[i]
        s += operationArr[i]
    return s + numArr[i + 1]


# ? Вычисление выражения
def get_evel(numArr: num_arr_type, operation_arr: operations_before_type) -> int:
    """
    Вычисляет значение выражения на основе списка чисел и списка операций.

    Parameters:
    - numArr (List[str]): Список чисел.
    - operationArr (List[str]): Список операций.

    Returns:
    - int: Значение выражения.
    """
    total_sum: int = 0
    for i in range(len(numArr)- 1):
        if i == 0:
            total_sum = int(numArr[i])
        else:
            if operation_arr[i - 1] == "+":
                total_sum += int(numArr[i])
            else:
                total_sum -= int(numArr[i])
    return total_sum


# ? Функция финального вывода
def final_return(
    num_arr: num_arr_type,
    operation_arr: operations_before_type,
    operaction: operaction_type,
) -> str:
    """
    Возвращает окончательное выражение в виде строки.

    Parameters:
    - num_arr (List[str]): Список чисел.
    - operation_arr (List[str]): Список операций.
    - operation (str): Результат операции ("end" или "no solution").

    Returns:
    - str: Окончательное выражение в виде строки.
    """
    if operaction == "no solution":
        return "no solution"
    return get_expression(num_arr, operation_arr) + "=" + num_arr[len(num_arr) - 1]


# ? Функция выбора варианта
def choose(
    num_arr_1: num_arr_type,
    operaions_before_1: operations_before_type,
    operation_1: operaction_type,
    num_arr_2: num_arr_type,
    operaions_before_2: operations_before_type,
    operation_2: operaction_type,
) -> recursion_return_type:
    """
    Выбирает между двумя вариантами результата рекурсивной функции.

    Parameters:
    - num_arr_1 (List[str]): Список чисел для первого варианта.
    - operaions_before_1 (List[str]): Список операций для первого варианта.
    - operation_1 (str): Результат операции для первого варианта ("end" или "no solution").
    - num_arr_2 (List[str]): Список чисел для второго варианта.
    - operaions_before_2 (List[str]): Список операций для второго варианта.
    - operation_2 (str): Результат операции для второго варианта ("end" или "no solution").

    Returns:
    - tuple[list[str], list[str], Literal["end", "no solution"]]: Кортеж с результатом выбора.
    """
    if operation_1 == "end":
        return (num_arr_1, operaions_before_1, "end")
    elif operation_2 == "end":
        return (num_arr_2, operaions_before_2, "end")
    return ([], [], "no solution")
