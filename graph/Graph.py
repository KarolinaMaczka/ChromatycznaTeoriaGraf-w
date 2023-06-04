class Graph:
    __slots__ = ["_vertices", "_edges", "_Delta", "_delta"]

    def __init__(self):
        self._vertices = []
        self._edges = []
        self._Delta = None
        self._delta = None

        return

    @property
    def vertices(self):
        return self._vertices

    @vertices.setter
    def vertices(self, p_new):
        pass

    @property
    def edges(self):
        return self._edges

    @edges.setter
    def edges(self, p_new):
        pass

    @property
    def Delta(self):
        return self._Delta

    @property
    def delta(self):
        return self._delta

    def _calculate_degrees(self):
        """
            Calculates degrees of every vertex in the graph and updates them.
        """
        for edge in self._edges:
            self._vertices[edge["v1"]].deg += 1
            self._vertices[edge["v2"]].deg += 1

        return

    def _refresh_deltas(self):
        """
        Refreshes Delta and delta properties of the graph.
        """
        if len(self._vertices) == 0:
            return

        self._delta = self._Delta = self._vertices[0].deg

        for vertex in self._vertices:
            if vertex.deg > self._Delta:
                self._Delta = vertex.deg

            if vertex.deg < self._delta:
                self._delta = vertex.deg

        return

    def __repr__(self):
        result = ""

        result += "V = {\n"
        for vertex in self._vertices:
            result += f"\t{vertex};\n"
        result += "}\n\n"

        result += "E = {\n"
        for edge in self._edges:
            result += f"\t({self._vertices[edge['v1']].name}; {self._vertices[edge['v2']].name});\n"
        result += "}\n\n"

        result += f"Delta(G) = {self.Delta}\n"
        result += f"delta(G) = {self.delta}"

        return result
