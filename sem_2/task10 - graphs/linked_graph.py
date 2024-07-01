import heapq
from vertex import Vertex
from link import Link
from typing import Union, Tuple


prev_type = Tuple[Union[Vertex, Link], Union[float, int]]


class LinkedGraph:
    def __init__(self):
        self._links: list[Link] = []
        self._vertex: list[Vertex] = []

    def add_vertex(self, v: Vertex):
        """
        Добавляет вершину v в граф, если она ещё не присутствует.

        Параметры:
        - v (Vertex): Вершина, которую необходимо добавить в граф.

        Возвращаемое значение:
        - None

        Примечания:
        - Если вершина v уже присутствует в графе, она не будет добавлена повторно.
        - Метод обновляет состояние графа, добавляя вершину к списку _vertex.
        """
        if v not in self._vertex:
            self._vertex.append(v)

    def add_link(self, link: Link):
        """
        Добавляет связь (ребро) link в граф, если она ещё не существует.

        Параметры:
        - link (Link): Связь (ребро), которую необходимо добавить в граф.

        Возвращаемое значение:
        - None

        Примечания:
        - Если связь link уже присутствует в графе (по сравнению существующих связей), она не будет добавлена повторно.
        - Если вершины link.v1 и link.v2 (концы связи) отсутствуют в графе, они также будут добавлены с помощью метода add_vertex.
        - Связь link будет добавлена к спискам связей (links) вершин link.v1 и link.v2.
        - Метод обновляет состояние графа, добавляя связь к списку _links и вершины к списку _vertex при необходимости.
        """
        if not any(l == link for l in self._links):
            self._links.append(link)
            if link.v1 not in self._vertex:
                self._vertex.append(link.v1)
            if link.v2 not in self._vertex:
                self._vertex.append(link.v2)
            link.v1.links.append(link)
            link.v2.links.append(link)

    def find_path(self, start_v, stop_v):
        """
        Находит кратчайший путь в графе между вершинами start_v и stop_v, используя алгоритм Дейкстры.

        Параметры:
        - start_v (Vertex): Начальная вершина пути.
        - stop_v (Vertex): Целевая вершина пути.

        Возвращаемое значение:
        - tuple[list[Vertex], list[Link]]: Кортеж из двух элементов:
            - Первый элемент - список вершин, представляющих кратчайший путь от start_v до stop_v.
            - Второй элемент - список связей (рёбер), составляющих этот кратчайший путь.

        Примечания:
        - Используется алгоритм Дейкстры для нахождения кратчайшего пути.
        - Если start_v или stop_v не являются экземплярами класса Vertex, либо если dist не является числом, возникает исключение NotImplemented.
        - Возвращает кортеж пустых списков, если путь между start_v и stop_v не найден.
        """

        dist = {v: float("inf") for v in self._vertex}
        previous: prev_type = {v: None for v in self._vertex}
        dist[start_v] = 0

        priority_queue = [(0, start_v)]
        while priority_queue:
            current_dist, current_vertex = heapq.heappop(priority_queue)

            if (
                not (isinstance(current_vertex, Vertex))
                or not (isinstance(stop_v, Vertex))
                or not isinstance(current_dist, (float, int))
            ):
                raise NotImplemented

            if current_vertex == stop_v:
                break

            for link in current_vertex.links:
                neighbor = link.v2 if link.v1 == current_vertex else link.v1
                new_dist = current_dist + link.dist

                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    previous[neighbor] = link
                    heapq.heappush(priority_queue, (new_dist, neighbor))

        path = []
        links = []
        current_vertex = stop_v
        while previous[current_vertex] is not None:
            path.append(current_vertex)
            links.append(previous[current_vertex])
            current_vertex = (
                previous[current_vertex].v1
                if previous[current_vertex].v2 == current_vertex
                else previous[current_vertex].v2
            )

        path.append(start_v)
        path.reverse()
        links.reverse()
        return path, links
