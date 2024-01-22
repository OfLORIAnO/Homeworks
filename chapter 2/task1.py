from typing import Tuple, List

def task1() -> str:
    # Получаем строку от пользователя
    s: str = input()
    
    # Список для хранения подстрок
    listOfSubs: List[str] = []
    
    # Список для отслеживания уникальных символов в текущей подстроке
    charsWas: List[str] = []
    
    # Временная строка для построения текущей подстроки без повторных символов
    tempString: str = ""

    # Проходим по каждому символу в строке
    for i in range(0, len(s)):
        char: str = s[i]
        
        # Если символ не встречался в текущей подстроке, добавляем его
        if char not in charsWas:
            tempString += char
        else:
            # Если символ уже встречался, завершаем текущую подстроку
            listOfSubs.append(tempString)
            
            # Начинаем новую подстроку с текущего символа
            tempString = char
            
            # Сбрасываем список уникальных символов
            charsWas = []

        # Добавляем текущий символ в список уникальных символов
        charsWas.append(char)

    # Добавляем последнюю подстроку в список
    listOfSubs.append(tempString)

    # Находим самую длинную подстроку
    maxLenWord: str = max(listOfSubs, key=len, default="")

    # Выводим результат
    print(maxLenWord)

    return maxLenWord



if __name__ == "__main__":
    task1()
