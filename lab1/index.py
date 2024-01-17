# ? Импорт модулей
from helper import get_evel, final_return, choose

# ? Импорт типов
from my_types import (
    num_arr_type,
    operations_before_type,
    recursion_return_type,
)


# ? Рекурсивная функция
def recursion_func(
    num_arr: num_arr_type,  # ? Список всех чисел
    operations_before: operations_before_type = [],  # ? Список знаков
) -> recursion_return_type:
    # ? Если все знаки уже расставлены
    if len(operations_before) == len(num_arr) - 2:
        # ? Если выражение равно ожидаемому
        if int(num_arr[len(num_arr) - 1]) == get_evel(num_arr, operations_before):
            return (num_arr, operations_before, "end")
        # ? Если выражение не равно ожидаемому, значит оно нам не подходит
        return ([], [], "no solution")

    # ? Продолжаем добирать
    return choose(
        *recursion_func(num_arr, operations_before + ["+"]),
        *recursion_func(num_arr, operations_before + ["-"]),
    )


if __name__ == "__main__":
    data = open("lab1/nums.txt").readline().split()[1::]

    print(
        final_return(*recursion_func(data))
    )  # ? Передаём в функцию последовательность без первого числа
