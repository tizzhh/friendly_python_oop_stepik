from typing import List, Tuple


class Link:
    def __init__(self, v1: 'Vertex', v2: 'Vertex') -> None:
        self._v1 = v1
        self._v2 = v2
        self._dist = 1

        if self not in v1.links:
            v1.links.append(self)

        if self not in v2.links:
            v2.links.append(self)

    def __eq__(self, other: 'Link') -> bool:
        return (self.v1 == other.v1 and self.v2 == other.v2) or (
            self.v1 == other.v2 and self.v2 == other.v1
        )

    @property
    def v1(self) -> 'Vertex':
        return self._v1

    @property
    def v2(self) -> 'Vertex':
        return self._v2

    @property
    def dist(self) -> int:
        return self._dist

    @dist.setter
    def dist(self, value: int) -> None:
        self._dist = value


class Vertex:
    def __init__(self) -> None:
        self._links: List[Link] = []

    @property
    def links(self) -> List[Link]:
        return self._links


class Station(Vertex):
    def __init__(self, name: str) -> None:
        super().__init__()
        self.name = name

    def __str__(self) -> str:
        return f'{self.name}'

    def __repr__(self) -> str:
        return f'{self.name}'


class LinkMetro(Link):
    def __init__(self, v1: Vertex, v2: Vertex, dist: int) -> None:
        super().__init__(v1, v2)
        self.dist = dist

    def __repr__(self) -> str:
        return f'{self.v1} <-> {self.v2}: {self.dist} km'


class LinkedGraph:
    def __init__(self) -> None:
        self._links: List[Link] = []
        self._vertex: List[Vertex] = []

    def add_vertex(self, v: Vertex) -> None:
        if v not in self._vertex:
            self._vertex.append(v)

    def add_link(self, link: Link) -> None:
        if any(lnk == link for lnk in self._links):
            return None
        self._links.append(link)

        v1, v2 = link.v1, link.v2
        if v1 not in self._vertex:
            self._vertex.append(v1)

        if v2 not in self._vertex:
            self._vertex.append(v2)

    def find_path(
        self, start_v: Vertex, stop_v: Vertex
    ) -> Tuple[List[Vertex], List[Link]]:
        best_path = None
        best_path_length = float('inf')

        def dfs(
            current_v: Vertex, current_path: List[Link], current_length: int
        ) -> None:
            nonlocal best_path, best_path_length

            if current_v == stop_v and current_length < best_path_length:
                best_path = current_path[:]
                best_path_length = current_length
                return

            for link in current_v.links:
                next_v = link.v1 if link.v2 == current_v else link.v2
                if link not in current_path:
                    dfs(
                        next_v,
                        current_path + [link],
                        current_length + link.dist,
                    )

        dfs(start_v, [], 0)
        vertexes = [start_v]
        for link in best_path:
            next_v = link.v1 if vertexes[-1] != link.v1 else link.v2
            vertexes.append(next_v)

        return (vertexes, best_path)


map_metro = LinkedGraph()
v1 = Station("Сретенский бульвар")
v2 = Station("Тургеневская")
v3 = Station("Чистые пруды")
v4 = Station("Лубянка")
v5 = Station("Кузнецкий мост")
v6 = Station("Китай-город 1")
v7 = Station("Китай-город 2")

map_metro.add_link(LinkMetro(v1, v2, 1))
map_metro.add_link(LinkMetro(v2, v3, 1))
map_metro.add_link(LinkMetro(v1, v3, 1))

map_metro.add_link(LinkMetro(v4, v5, 1))
map_metro.add_link(LinkMetro(v6, v7, 1))

map_metro.add_link(LinkMetro(v2, v7, 5))
map_metro.add_link(LinkMetro(v3, v4, 3))
map_metro.add_link(LinkMetro(v5, v6, 3))
path = map_metro.find_path(v1, v6)

print(path[0], path[1])
