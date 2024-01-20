from itertools import product

nums_dict: dict[str, str] = {
    "1": "124",
    "2": "1235",
    "3": "236",
    "4": "1457",
    "5": "24568",
    "6": "3569",
    "7": "478",
    "8": "57890",
    "9": "68",
}


def get_pins(pin: str) -> list[str]:
    """
    Мы крутые взломщики, но мы слепые, поэтому гадаем тут на картах, как женщины в тике токе

    Args:
        pin (str): Пинкод, который мы увидели

    Returns:
        list[str]: Список всех возможных вариантов
    """

    return list(map(lambda x: "".join(x), product(*[nums_dict[sym] for sym in pin])))

# ? Во как теперь могу
get_variants = lambda pin: list(map(lambda x: "".join(x), product(*[nums_dict[sym] for sym in pin])))



if __name__ == "__main__":
    print(get_variants("11"))
    print(get_pins("11"))
