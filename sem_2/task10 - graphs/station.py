from vertex import Vertex


class Station(Vertex):
    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта Station.

        Возвращаемое значение:
        - str: Имя станции (атрибут name).

        Примечания:
        - Метод вызывается при использовании функции str() для объекта Station.
        """
        return self.name

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта Station для его представления в Python.

        Возвращаемое значение:
        - str: Имя станции (атрибут name).

        Примечания:
        - Метод вызывается при использовании функции repr() для объекта Station.
        """
        return self.name

    def __lt__(self, other: object):
        """
        Оператор меньше (<) для сравнения станций на основе их имен.

        Параметры:
        - other (object): Другой объект для сравнения.

        Возвращаемое значение:
        - bool: True, если текущая станция (self) имеет лексикографически меньшее имя, чем у другой станции (other).
                False в противном случае.

        Примечания:
        - Если other не является экземпляром класса Station, возникает исключение NotImplemented.
        """
        if not isinstance(other, Station):
            raise NotImplemented
        return self.name < other.name
