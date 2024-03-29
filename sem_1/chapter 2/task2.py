def reverseWords(s: str) -> str:
    """
    Инвертирует порядок слов в строке.

    Args:
    - s (str): Входная строка.

    Returns:
    - str: Строка с инвертированным порядком слов.
    """

    tempString: str = ""
    l: int = 0

    for i in range(len(s)):
        if s[i] == " ":
            tempString = s[l:i] + " " + tempString
            l = i + 1
        if i == len(s) - 1:
            tempString = s[l : len(s)] + " " + tempString

    return tempString


def deleteSpaces(s: str) -> str:
    """
    Удаляет лишние пробелы из строки.

    Args:
    - s (str): Входная строка.

    Returns:
    - str: Строка без лишних пробелов.
    """

    tempString: str = ""

    for i in range(len(s) - 1):
        if s[i] == " " and s[i + 1] == " ":
            continue
        else:
            tempString = tempString + s[i]

    return tempString


def convert() -> str:
    """
    Объединяет функции инверсии слов и удаления лишних пробелов, приводит к нижнему регистру,
    и делает первую букву строки заглавной.

    Returns:
    - str: Результат преобразования входной строки.
    """

    s: str = input()
    return deleteSpaces(reverseWords(s.strip().lower())).capitalize()


if __name__ == "__main__":
    convert()
