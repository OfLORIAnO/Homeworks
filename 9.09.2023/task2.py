from task1 import getLenOfNum

def reverseNum(num):
    
    isNegative = False
    if num < 0:
        isNegative = True
        num = abs(num)

    newNum = 0
    while num > 0:
        lastDigit = num % 10
        if lastDigit == 0:
            num //= 10
            continue
        newNum += 10 ** (getLenOfNum(num) - 1) * lastDigit
        num //= 10

    if isNegative:
        newNum *= -1
    if not((-2**7) <= newNum <= (2**7-1)):
        return "no solution"
    
    return newNum

if __name__ == "__main__":
    print(reverseNum(12))
    print(reverseNum(123))
    print(reverseNum(-150))
    print(reverseNum(101))
    print(reverseNum(-110))