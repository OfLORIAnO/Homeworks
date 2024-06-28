from cell import Cell
from tictactoe import TicTacToe


cell = Cell()
assert (
    cell.value == 0
), "начальное значение атрибута value объекта класса Cell должно быть равно 0"
assert bool(cell), "функция bool для объекта класса Cell вернула неверное значение"
cell.value = 1
assert (
    bool(cell) == False
), "функция bool для объекта класса Cell вернула неверное значение"
assert (
    hasattr(TicTacToe, "show")
    and hasattr(TicTacToe, "human_go")
    and hasattr(TicTacToe, "computer_go")
), "класс TicTacToe должен иметь методы show, human_go, computer_go"
game = TicTacToe()
assert bool(game), "функция bool вернула неверное значения для объекта класса TicTacToe"
assert (
    game[0, 0] == 0 and game[2, 2] == 0
), "неверные значения ячеек, взятые по индексам"
game[1, 1] = TicTacToe.HUMAN_X
assert (
    game[1, 1] == TicTacToe.HUMAN_X
), "неверно работает оператор присваивания нового значения в ячейку игрового поля"
game[0, 0] = TicTacToe.COMPUTER_O
assert (
    game[0, 0] == TicTacToe.COMPUTER_O
), "неверно работает оператор присваивания нового значения в ячейку игрового поля"
game.init()
assert (
    game[0, 0] == TicTacToe.FREE_CELL and game[1, 1] == TicTacToe.FREE_CELL
), "при инициализации игрового поля все клетки должны принимать значение из атрибута FREE_CELL"
try:
    game[3, 0] = 4
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"
game.init()
assert (
    game.is_human_win == False
    and game.is_computer_win == False
    and game.is_draw == False
), "при инициализации игры атрибуты is_human_win, is_computer_win, is_draw должны быть равны False, возможно не пересчитывается статус игры при вызове метода init()"
game[0, 0] = TicTacToe.HUMAN_X
game[1, 1] = TicTacToe.HUMAN_X
game[2, 2] = TicTacToe.HUMAN_X
assert (
    game.is_human_win and game.is_computer_win == False and game.is_draw == False
), "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"
game.init()
game[0, 0] = TicTacToe.COMPUTER_O
game[1, 0] = TicTacToe.COMPUTER_O
game[2, 0] = TicTacToe.COMPUTER_O
assert (
    game.is_human_win == False and game.is_computer_win and game.is_draw == False
), "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"
print("passed")
