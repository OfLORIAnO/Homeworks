from link import Link
from vertex import Vertex


class LinkMetro(Link):
    def __init__(self, v1: Vertex, v2: Vertex, dist: int):
        super().__init__(v1, v2, dist)
