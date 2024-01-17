from typing import Tuple, Literal

# ? Создаём типы
existing_figures_type = list[Tuple[int, int]]
symbol_type = Literal["#", "*", "0"]
board_type = list[list[symbol_type]]
solutions_type = list[Tuple[int, int]]
total_solutions_type = list[solutions_type]
