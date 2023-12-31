from typing import Literal


def rotateMatrix(matrix: list[list[int]]) -> None:
    matrix.reverse()  # ? reverse horiaontal
    for i in range(len(matrix)):
        matrix[i].reverse()  # ? reverse vertical


def spiral(matrix: list[list[int]]) -> list[int]:
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
