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
    """
    Рекурсивная функция для поиска выражения, соответствующего заданному результату.

    Параметр: num_arr: Список всех чисел.
    Параметр: operations_before: Список знаков.

    Возвращает: Кортеж, содержащий текущую расстановку чисел, знаков и информацию о состоянии ("end" или "no solution").
    """
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


def main():
    """def main() -> None:
    Основная функция программы.

    Читает данные из файла "lab1/nums.txt",удаляет первое число,
    передает последовательность чисел в рекурсивную функцию,
    получает результат и выводит его на экран.
    """
    data = open("lab1/nums.txt").readline().split()[1::]

    print(
        final_return(*recursion_func(data))
    )  # ? Передаём в функцию последовательность без первого числа


if __name__ == "__main__":
    main()
