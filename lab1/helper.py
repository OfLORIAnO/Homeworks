from typing import Union


def get_evel(numArr: list[str], operationArr: list[str]) -> Union[int, False]:
    try:
        s: str = ""
        for i in range(len(operationArr)):
            s += numArr[i]
            s += operationArr[i]
        s += numArr[i + 1]
        return eval(s)
    except:
        return False


def get_num(num: str) -> str:
    if int(num) < 0:
        return f" ({num}) "
    else:
        return num


def final_return(
    numArr: list[str], operationArr: list[str], expressionEquals: str
) -> str:
    s: str = ""
    for i in range(len(operationArr)):
        s += get_num(numArr[i])
        s += f" {operationArr[i]} "
    s += get_num(numArr[i + 1]) + " = " + expressionEquals
    return s
