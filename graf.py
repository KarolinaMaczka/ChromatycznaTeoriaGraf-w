import random
import math

import matplotlib.pyplot as plt
from matplotlib.patches import Circle as pltCircle

class Circle:
    def __init__(self, point, r):
        self.point = point
        self.r = r

    def intersect(self, other):
        distance = math.sqrt(sum((self.point[i]-other.point[i])**2 for i in range(len(self.point))))
        return distance < self.r + other.r

    def __repr__(self):
        return f'{self.point}'

class Graph:
    def __init__(self, dimension, amount, max_range):
        self.dimension = dimension
        self.amount = amount
        self.max_range = max_range
        self.points = [Circle([random.random()* max_range for _ in range(dimension)],1) for _ in range(amount)]
        self.edges = self.circle_intersection_graph()

    def __repr__(self):
        text='Punkty w grafie: \n'
        for c in self.points:
            text+= c.__repr__()
            text += ', '

        return text

    def circle_intersection_graph(self):
        edges = set()
        for i in range(self.amount):
            for j in range(i+1, self.amount):
                if self.points[i].intersect(self.points[j]):
                    edges.add((i, j))
        return edges

# function plotting only circles
def plot_circles(G):
    circles = G.points
    fig, ax = plt.subplots()
    ax.set_xlim(-2, G.max_range + 2)
    ax.set_ylim(-2, G.max_range + 2)
    for circle in circles:
        ax.add_artist(pltCircle(circle.point, circle.r, fill=False))
    ax.set_aspect('equal')
    plt.show()

# function plotting circles with edges
def plot_circle_intersection_graph(G):
    fig, ax = plt.subplots()
    ax.set_xlim(-2, G.max_range + 2)
    ax.set_ylim(-2, G.max_range + 2)
    circles = G.points
    for circle in circles:
        ax.add_artist(pltCircle(circle.point, circle.r, fill=False))
    for edge in G.edges:
        ax.plot([circles[edge[0]].point[0], circles[edge[1]].point[0]],
                [circles[edge[0]].point[1], circles[edge[1]].point[1]], '-k')
    ax.set_aspect('equal')
    plt.show()

G = Graph(2, 5, 10)
print(G)

plot_circles(G)
plot_circle_intersection_graph(G)