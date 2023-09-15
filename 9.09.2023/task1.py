def getLenOfNum(num):
    cnt = 0
    while num > 0:
        cnt += 1
        num //= 10
    return cnt

def palindrome(num):
    if num < 0:
        num = abs(num)
    if getLenOfNum(num) == 1: #? Если длина числа 1, то фиг знает полигон ли это, так что пусть будет да
        return True
    while num > 0:
        r = num % 10 #? Получаем правый символ
        num = int(num // 10) #? Срезаем правый символ

        lenNum = getLenOfNum(num) #? Получаем длину числа
        
        l = int(num // 10**(lenNum-1)) #? Получаем левый символ
        num = int(num % 10**(lenNum-1)) #? Срезаем левый символ

        if getLenOfNum(num) == 1: #? Если длина числа 1, то либо остался последний символ, либо число изначально было длины 3
            if l == r:
                return True
            elif l == 0 or r == 0:
                return False
            return False
        if l != r: #? Ну тут очевидно всё
            return False
    #? Если мы дошли до сюда, значит всё хорошо 😎😎
    return True

if __name__ == "__main__":
    print("Тесты 👇")
    print("1:", palindrome(5)) #! True
    print("2:", palindrome(0)) #! True
    print("3:", palindrome(9)) #! True
    print("4:", palindrome(121)) #! True
    print("5:", palindrome(1221)) #! True
    print("6:", palindrome(12321)) #! True
    print("7:", palindrome(123)) #! False
    print("8:", palindrome(1234)) #! False
    print("9:", palindrome(12345)) #! False
    print("10:", palindrome(1234567890987654321)) #! True
    print("11:", palindrome(123456789098765432)) #! False
    print("12:", palindrome(98765432123456789)) #! True
    print("13:", palindrome(-5)) #! True