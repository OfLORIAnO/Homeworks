roman_numerals_type = list[tuple[str, int]]


def func(num: int) -> str:
    """
    Преобразует арабское число в римскую систему.

    Параметры:
    - num: Целое число в диапазоне от 1 до 3999.

    Возвращает:
    - Строка, представляющая арабское число в римской системе.
    """
    # ? Проверка допустимости входного числа
    if not (0 < num < 4000):
        return "Число должно быть в пределах от 1 до 3999"

    # ? Определение римских цифр с их эквивалентами в арабской системе
    roman_numerals: roman_numerals_type = [
        ("M", 1000),
        ("CM", 900),
        ("D", 500),
        ("CD", 400),
        ("C", 100),
        ("XC", 90),
        ("L", 50),
        ("XL", 40),
        ("X", 10),
        ("IX", 9),
        ("V", 5),
        ("IV", 4),
        ("I", 1),
    ]

    result: str = ""

    # ? Преобразование числа в римскую систему
    for numeral, value in roman_numerals:
        while num >= value:
            result += numeral
            num -= value

    return result


if __name__ == "__main__":
    print(func(19))
