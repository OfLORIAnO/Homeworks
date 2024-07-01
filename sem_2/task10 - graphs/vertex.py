from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from link import Link


class Vertex:
    _id_counter = 0

    def __init__(self):
        self._links: list["Link"] = []
        self.id = Vertex._id_counter
        Vertex._id_counter += 1

    @property
    def links(self) -> list["Link"]:
        """
        Свойство, возвращающее список связей (рёбер), инцидентных данной вершине.

        Возвращаемое значение:
        - list["Link"]: Список объектов Link, представляющих связи (рёбра), инцидентные данной вершине.
        """
        return self._links

    def __lt__(self, other: object) -> bool:
        """
        Оператор меньше (<) для сравнения вершин на основе их идентификаторов.

        Параметры:
        - other (object): Другой объект для сравнения.

        Возвращаемое значение:
        - bool: True, если текущая вершина (self) имеет меньший идентификатор, чем другая вершина (other).
                False в противном случае.

        Примечания:
        - Если other не является экземпляром класса Vertex, возникает исключение NotImplemented.
        """
        if not isinstance(other, Vertex):
            raise NotImplemented

        return self.id < other.id
