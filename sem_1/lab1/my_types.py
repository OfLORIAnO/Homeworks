from typing import Literal


num_arr_type = list[str]
operations_before_type = list[str]
operaction_type = Literal["+", "-", "end", "no solution"]

recursion_return_type = tuple[num_arr_type, operations_before_type, operaction_type]
