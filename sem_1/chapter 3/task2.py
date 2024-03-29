from typing import List


def rotateMatrix(matrix: List[List[int]]) -> List[List[int]]:
    """
    Поворачивает матрицу на 90 градусов по часовой стрелке.

    Args:
    - matrix (List[List[int]]): Входная матрица.

    Returns:
    - List[List[int]]: Новая матрица, повернутая на 90 градусов по часовой стрелке.
    """

    newList: List[List[int]] = []

    # Выравниваем матрицу по горизонтали
    for d in range(len(matrix)):
        if len(matrix) > len(matrix[d]):
            matrix[d].append(0)
        elif len(matrix) < len(matrix[d]):
            matrix.append([0] * len(matrix[d]))

    # Транспонируем матрицу
    for i in range(len(matrix)):
        for j in range(i, len(matrix[i])):
            if len(matrix) > len(matrix[i]):
                matrix[i].append(0)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Формируем новую матрицу без пустых строк и столбцов
    for i in range(len(matrix)):
        if matrix[i] == [0] * len(matrix[0]):
            matrix.pop()
            continue
        elif matrix[i][len(matrix[i]) - 1] == 0:
            newList.append(matrix[i][0 : len(matrix[i]) - 1])
            continue

    # Возвращаем новую матрицу, если она не пуста, иначе возвращаем исходную матрицу
    if newList:
        return newList
    return matrix


if __name__ == "__main__":
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]
    matrix2 = [
        [1, 2, 3],
        [5, 6, 7],
        [9, 10, 11],
    ]
    matrix3 = [[1, 2], [3, 4], [5, 6]]
    print(rotateMatrix(matrix))
    print("-----------------------------")
    print(rotateMatrix(matrix2))
    print("-----------------------------")
    print(rotateMatrix(matrix3))
    pass
