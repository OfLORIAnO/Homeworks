from typing import Literal, List


def rotateMatrix(matrix: List[List[int]]) -> None:
    """
    Поворачивает матрицу

    Args:
    - matrix (List[List[int]]): Входная матрица.

    Returns:
    - None
    """
    matrix.reverse()  # reverse horizontal
    for i in range(len(matrix)):
        matrix[i].reverse()  # reverse vertical


def spiral(matrix: List[List[int]]) -> List[int]:
    """
    Обходит матрицу по спирали, начиная с левого верхнего угла и двигаясь по часовой стрелке.

    Args:
    - matrix (List[List[int]]): Входная матрица.

    Returns:
    - List[int]: Список значений, полученных при обходе матрицы по спирали.
    """

    string = ""
    mode: Literal["hor", "vert"] = "hor"
    while len(matrix):
        if mode == "hor":
            for x in matrix[0]:
                string += str(x)
            matrix.remove(matrix[0])
            mode = "vert"
        elif mode == "vert":
            for y in range(len(matrix)):
                string += str(matrix[y].pop())
            rotateMatrix(matrix)
            mode = "hor"
    return list(map(int, string))


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(spiral(matrix))
