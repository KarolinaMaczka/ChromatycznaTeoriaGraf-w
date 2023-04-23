from matplotlib import pyplot as plt
from matplotlib.patches import Circle as pltCircle

from const import *
from geom.Circle import Circle
from graph.Graph import Graph
from graph.Vertex import Vertex


class IntersectionGraph(Graph):
    @staticmethod
    def get_intersection_graph(p_list_of_circles):
        assert isinstance(p_list_of_circles, list)
        for circle in p_list_of_circles:
            assert isinstance(circle, Circle)

        res = IntersectionGraph()

        for circle in p_list_of_circles:
            res.vertices.append(Vertex(circle))

        i = 0
        while i < len(res.vertices):
            j = i + 1
            while j < len(res.vertices):
                if res.vertices[i].info.intersects_with(res.vertices[j].info):
                    res.edges.append({"v1": i, "v2": j})

                j += 1
            i += 1

        res._calculate_degrees()
        res._refresh_deltas()

        return res

    def plot_circles(self):
        fig, ax = plt.subplots()
        ax.set_xlim(RANGE_FROM - RADIUS - 1, RANGE_TO + RADIUS + 1)
        ax.set_ylim(RANGE_FROM - RADIUS - 1, RANGE_TO + RADIUS + 1)

        for vertex in self.vertices:
            ax.add_artist(pltCircle((vertex.info.pos_x, vertex.info.pos_y), vertex.info.radius, fill=False))

        ax.set_aspect('equal')
        plt.show()

        return

    def plot_circle_intersection_graph(self):
        fig, ax = plt.subplots()
        ax.set_xlim(RANGE_FROM - RADIUS - 1, RANGE_TO + RADIUS + 1)
        ax.set_ylim(RANGE_FROM - RADIUS - 1, RANGE_TO + RADIUS + 1)

        for vertex in self.vertices:
            ax.add_artist(pltCircle((vertex.info.pos_x, vertex.info.pos_y), vertex.info.radius, fill=False))
            ax.plot(vertex.info.pos_x, vertex.info.pos_y, marker="o", color=COLOURS[vertex.colour], markersize=10)

        for edge in self.edges:
            ax.plot([self.vertices[edge["v1"]].info.pos_x, self.vertices[edge["v2"]].info.pos_x],
                    [self.vertices[edge["v1"]].info.pos_y, self.vertices[edge["v2"]].info.pos_y],
                    "-k")

        ax.set_aspect('equal')
        plt.show()

        return

    def colour_disc_graph(self):
        sor = [el[0] for el in sorted(enumerate(self.vertices), key=lambda x: x[1].info.pos_x)]
        self.colour_greed(sor)

        return

    def colour_greed(self, p_order):
        colours = set(i for i in range(self.Delta + 1))

        for i in p_order:
            self._colour_vertex(self._vertices[i], colours)

        pass

    def _colour_vertex(self, p_vertex, p_set_of_colours):
        neighbours_colours = set()

        for edge in self._edges:
            if p_vertex == self._vertices[edge["v1"]]:
                neighbours_colours.add(self._vertices[edge["v2"]].colour)
                continue

            if p_vertex == self._vertices[edge["v2"]]:
                neighbours_colours.add(self._vertices[edge["v1"]].colour)

        available_colors = p_set_of_colours - neighbours_colours

        p_vertex.colour = min(available_colors)

        return

    def used_colours_set(self):
        result = set()

        for vertex in self._vertices:
            result.add(vertex.colour)

        return result

    def pseudo_chi(self):
        return len(self.used_colours_set())

    def __repr__(self):
        result = super().__repr__()

        result += "\n\n"

        result += f"chi*(G) = {self.pseudo_chi()}"

        return result
