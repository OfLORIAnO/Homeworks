# ? Импорт модулей
from helper import get_evel, final_return, choose

# ? Импорт типов
from myTypes import (
    num_arr_type,
    operaions_before_type,
    recursion_return_type,
)


def output_data(list1: num_arr_type) -> str:
    return final_return(
        *choose(*recursion_func(list1, ["+"]), *recursion_func(list1, ["-"])),
        list1[len(list1) - 1],
    )


# ? Рекурсивная функция
def recursion_func(
    num_arr: num_arr_type,  # ? Список всех чисел
    operaions_before: operaions_before_type,  # ? Список знаков
) -> recursion_return_type:
    expression_equals: int = int(num_arr[len(num_arr) - 1])

    # ? Если Все знаки уже расставлены
    if len(operaions_before) == len(num_arr) - 2:
        # ? То, чему должно быть равно выражение
        totalAns = get_evel(num_arr, operaions_before)
        if expression_equals == totalAns:  # ? Если выражение равно ожидаемому
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
