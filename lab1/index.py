# ? Импорт модулей
from helper import get_evel, final_return, choose

# ? Импорт типов
from my_types import (
    num_arr_type,
    operaions_before_type,
    recursion_return_type,
)


def output_data(list1: num_arr_type) -> str:
    return final_return(*recursion_func(list1))


# ? Рекурсивная функция
def recursion_func(
    num_arr: num_arr_type,  # ? Список всех чисел
    operaions_before: operaions_before_type = [],  # ? Список знаков
) -> recursion_return_type:
    # ? Если все знаки уже расставлены
    if len(operaions_before) == len(num_arr) - 2:
        # ? Если выражение равно ожидаемому
        if int(num_arr[len(num_arr) - 1]) == get_evel(num_arr, operaions_before):
            return (num_arr, operaions_before, "end")
        # ? Если выражение не равно ожидаемому, значит оно нам не подходит
        return ([], [], "no solution")

    # ? Продолжаем перебирать
    return choose(
        *recursion_func(num_arr, operaions_before + ["+"]),
        *recursion_func(num_arr, operaions_before + ["-"]),
    )


if __name__ == "__main__":
    print(
        output_data(
            open("lab1/nums.txt")
            .readline()
            .split()[1 : len(open("lab1/nums.txt").readline().split())]
        )
    )  # ? Передаём в функцию последовательность без первого числа
