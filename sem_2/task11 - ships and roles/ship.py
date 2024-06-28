from typing import Tuple, Literal, Union

go_type = Literal[-1, 1]
tp_type = Literal[1, 2]
axis_type = Union[int, None]
axises_type_init = Tuple[axis_type, axis_type]
axises_type = Tuple[int, int]

ships_init = {4: 1, 3: 2, 2: 3, 1: 4}


class Ship:
    _x: axis_type = None
    _y: axis_type = None
    _length: int
    _tp: tp_type
    _is_move: bool = True
    _cells: list[int] = []
    _not_available_area: list[Tuple[int, int]] = []

    def __init__(
        self,
        length: int,
        tp: tp_type = 1,
        x: axis_type = None,
        y: axis_type = None,
    ):
        self._length = length
        self._tp = tp
        self._cells = [1 for _ in range(length)]
        if x is not None and y is not None:
            self.set_start_coords(x, y)
        self.set_is_not_available_area()

    def __getitem__(self, indx: int):
        if indx >= len(self._cells):
            raise IndexError("неверный индекс")
        return self._cells[indx]

    def __setitem__(self, indx, value: int):
        if indx >= len(self._cells):
            raise IndexError("неверный индекс")
        self._cells[indx] = value

    def set_is_not_available_area(self) -> None:
        self._not_available_area = []

        if self._x is None or self._y is None:
            return

        for cell in range(-1, self._length + 1):
            if self._tp == 1:
                x = self._x + cell
                y = self._y
                if self._is_out_of_pole(x, y):
                    self._not_available_area.append((x, y))
                if self._is_out_of_pole(x, y + 1):
                    self._not_available_area.append((x, y + 1))
                if self._is_out_of_pole(x, y - 1):
                    self._not_available_area.append((x, y - 1))
            else:
                x = self._x
                y = self._y + cell
                if self._is_out_of_pole(x, y):
                    self._not_available_area.append((x, y))
                if self._is_out_of_pole(x + 1, y):
                    self._not_available_area.append((x + 1, y))
                if self._is_out_of_pole(x - 1, y):
                    self._not_available_area.append((x - 1, y))

    def get_not_available_area(self) -> list[Tuple[int, int]]:
        return self._not_available_area

    def _is_out_of_pole(self, x: int, y: int) -> bool:
        return 0 <= x < 10 and 0 <= y < 10

    def set_start_coords(self, x: int, y: int):
        self._x = x
        self._y = y

    def get_start_coords(self) -> axises_type_init:
        return (self._x, self._y)

    def get_occupied_cells(self) -> list[axises_type]:
        if self._x is None or self._y is None:
            return []

        cells = list()
        self.get_start_coords()
        for i in range(self._length):
            if self._tp == 1:
                cells.append((self._x + i, self._y))
            else:
                cells.append((self._x, self._y + i))
        return cells

    def move(self, go: go_type) -> None:
        if (not (self._is_move)) or (not (self._x)) or (not (self._y)):
            return

        if go == 1:
            if self._tp == 1:
                self._x += 1
            else:
                self._y += 1
        else:
            if self._tp == 1:
                self._x -= 1
            else:
                self._y -= 1
        self.set_is_not_available_area()

    def is_collide(self, ship: "Ship"):
        ships_not_available_area = ship.get_occupied_cells()
        self_not_available_area = self.get_not_available_area()
        for not_available_cell in ships_not_available_area:
            if not_available_cell in self_not_available_area:
                return True
        return False

    def is_out_pole(self, size: int):
        if self._x is None or self._y is None:
            return NameError("координаты не заданы")

        startX, endX, startY, endY = 0, 0, 0, 0
        if self._tp == 1:
            startX = self._x
            endX = self._x + self._length - 1
            startY = self._y
            endY = self._y
        else:
            startX = self._x
            endX = self._x
            startY = self._y
            endY = self._y + self._length - 1
        return not (
            self._is_pos_out_of_pole(startX, startY, size)
            and self._is_pos_out_of_pole(endX, endY, size)
        )

    def _is_pos_out_of_pole(self, x, y, size=10):
        return 0 <= x < size - 1 and 0 <= y < size - 1
