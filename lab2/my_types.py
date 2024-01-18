from typing import Tuple, Literal
from numpy import ndarray

# ? Создаём типы
existing_figures_type = list[Tuple[int, int]]
symbol_type = Literal["#", "*", "0"]
board_type = ndarray
solutions_type = list[Tuple[int, int]]
total_solutions_type = list[solutions_type]
