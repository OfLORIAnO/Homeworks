from vertex import Vertex
from typing import Union


class Link:
    def __init__(self, v1: Vertex, v2: Vertex, dist: Union[float, int] = 1):
        self._v1 = v1
        self._v2 = v2
        self._dist = dist

    @property
    def v1(self) -> Vertex:
        """
        Свойство, возвращающее первую вершину (конец) связи (ребра).

        Возвращаемое значение:
        - Vertex: Первая вершина (конец) связи (ребра) типа Vertex.
        """
        return self._v1

    @property
    def v2(self) -> Vertex:
        """
        Свойство, возвращающее вторую вершину (конец) связи (ребра).

        Возвращаемое значение:
        - Vertex: Вторая вершина (конец) связи (ребра) типа Vertex.
        """
        return self._v2

    @property
    def dist(self) -> Union[float, int]:
        """
        Свойство, возвращающее дистанцию (вес) связи (ребра).

        Возвращаемое значение:
        - Union[float, int]: Дистанция (вес) связи (ребра), может быть числом с плавающей точкой или целым числом.
        """
        return self._dist

    @dist.setter
    def dist(self, value):
        """
        Setter для свойства dist, устанавливающий новое значение дистанции (веса) связи (ребра).

        Параметры:
        - value: Новое значение дистанции (веса) связи (ребра).
        """
        self._dist = value

    def __eq__(self, other: object) -> bool:
        """
        Оператор равенства (==) для сравнения двух связей (рёбер).

        Параметры:
        - other (object): Другой объект для сравнения.

        Возвращаемое значение:
        - bool: True, если текущая связь (self) и другая связь (other) имеют одни и те же вершины (в любом порядке).
                False в противном случае.

        Примечания:
        - Если other не является экземпляром класса Link, возникает исключение NotImplemented.
        """
        if not isinstance(other, Link):
            raise NotImplemented
        return (self.v1, self.v2) == (other.v1, other.v2) or (self.v1, self.v2) == (
            other.v2,
            other.v1,
        )
