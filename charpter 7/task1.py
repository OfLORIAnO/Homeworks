from typing import Union

users_dict_type = dict[str, Union[None, int]]


def santa_users(users: list) -> users_dict_type:
    """
    Функция принимает список пользователей в формате [userName, userIndex],
    где userName - строка, userIndex - число или ничего.
    Возвращает словарь, где ключи - имена пользователей, а значения - соответствующие индексы.
    Если индекс отсутствует, соответствующее значение равно None.

    Параметры: users: Список пользователей в формате [userName, userIndex].

    Возвращает: Словарь с именами пользователей и соответствующими индексами.
    """
    
    users_dict: users_dict_type = dict()

    for user in users:
        userName: str = user[0]
        userIndex: Union[None, int] = int(user[1]) if len(user) > 1 else None
        users_dict[userName] = userIndex

    return users_dict


if __name__ == "__main__":
    print(
        santa_users(
            [
                ["name1 surname1", 12345],
                ["name2 surname2"],
                ["name3 surname3", 12354],
                ["name4 surname4", 12435],
            ]
        )
    )
