from ship import Ship
from typing import Tuple
from random import randint

ships_init = {4: 1, 3: 2, 2: 3, 1: 4}


class GamePole:
    _size: int = 10
    _ships: list[Ship] = []
    _not_available_area: list[Tuple[int, int]] = list()

    def __init__(
        self,
        size: int = 10,
    ):
        self._size = size
        self._ships = []

    def init(self):
        self.generate_ships()
        # self.randomize_ships_positions()

    def get_ships(self) -> list[Ship]:
        return self._ships

    def __add_ship(self, ship: "Ship") -> None:
        self._ships.append(ship)

    def generate_ships(self) -> None:
        for length in ships_init.keys():
            count = ships_init[length]
            for _ in range(count):
                ship = Ship(length, randint(1, 2))
                placed = False
                while not placed:
                    startX = randint(0, self._size - 1)
                    startY = randint(0, self._size - 1)
                    ship.set_start_coords(startX, startY)
                    if not ship.is_out_pole(self._size) and not any(
                        ship.is_collide(old_ship) for old_ship in self._ships
                    ):
                        self._ships.append(ship)
                        placed = True

    def get_random_ship(self, ship: "Ship") -> Ship:
        return self._ships[randint(0, len(self._ships) - 1)]

    def __get_occupied_cells(self) -> list[Tuple[int, int]]:
        occupied_cells: list[Tuple[int, int]] = []
        for ship in self._ships:
            ships_occupied_cells = list(ship.get_occupied_cells())
            for cell in ships_occupied_cells:
                occupied_cells.append(cell)
        return occupied_cells

    def _set_is_not_available_area(self):
        not_available_cells: list[Tuple[int, int]] = []
        for ship in self._ships:
            for _ship_cell in ship.get_not_available_area():
                not_available_cells.append(_ship_cell)
        self._not_available_area = not_available_cells

    def _get_not_available_area(self):
        return self._not_available_area

    def show(self):
        self._set_is_not_available_area()
        not_available_cells = self._get_not_available_area()

        occupied_cells = self.__get_occupied_cells()
        view = ""
        for x in range(self._size):
            for y in range(self._size):
                if (x, y) in occupied_cells:
                    view += "1"
                    continue
                if (x, y) in not_available_cells:
                    view += "#"
                else:
                    view += "0"
            view += "\n"
        print(view)

    def get_pole(self):
        # ? так и не понял, что тут должно быть
        total_pole = tuple()
        for x in range(self._size):
            x_pole = tuple()
            for y in range(self._size):
                x_pole += ((x, y),)
            total_pole += (x_pole,)
        print(total_pole)
        return total_pole

    def move_ships(self):
        pass
