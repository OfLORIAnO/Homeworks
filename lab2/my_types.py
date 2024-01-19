from typing import Tuple, Literal
from numpy import ndarray

# ? Создаём типы
symbol_type = Literal["#", "*", "0"]
board_type = ndarray
solutions_type = list[Tuple[int, int]]
total_solutions_type = list[solutions_type]
