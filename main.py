import random

import pandas as pd

from const import *
from geom.Circle import Circle
from graph.IntersectionGraph import IntersectionGraph


def create_random_graphs(max_radius, max_num_circles, num_graph, max_range=None):
    """
            Creates a list of randomly initialized graphs.

    :param max_radius: maximum radius of circles, should not be smaller 0.5
    :param max_num_circles: how many circles are supposed to be initiated
    :param num_graph: how many graphs do we want to test
    :param max_range: maximum range of x and y axes
    :return:
        List of graphs
    """
    # list of graphs
    g = IntersectionGraph.get_intersection_graph([Circle(0, 0, 1)])
    graphs = [g for _ in range(num_graph)]

    # creating random graphs
    for i in range(num_graph):
        # initializing circles
        if max_range is None:
            circles = [Circle(rand(0, max_radius * 5), rand(0, max_radius * 5), random.uniform(0.5, max_radius)) for _
                       in range(random.randint(max(0, max_num_circles - 5), max_num_circles))]
        else:
            circles = [Circle(rand(0, max_range), rand(0, max_range), random.uniform(0.5, max_radius)) for _
                       in range(random.randint(max(1, max_num_circles - 5), max_num_circles))]
        # initializing graph from those circles
        graphs[i] = IntersectionGraph.get_intersection_graph(circles)

    return graphs


def colouring_test(max_radius, max_num_circles, num_graph, max_range=None):
    """
        Tests colouring of intersection graphs, writes to files graphs and dataframes with colouring.
    Figures with graphs are in the directory figures, named graph_{max_radius}_{number}.png.
    Dataframes with properties of those graphs are in the directory dataframes, named dataframe_{max_radius}.xlsx
    There can be trouble with using more than 20 colours, since a set of colours used to plot graph has 20 colours in it.

    :param max_radius: maximum radius of circles, should not be smaller 0.5
    :param max_num_circles: how many circles are supposed to be initiated
    :param num_graph: how many graphs do we want to test
    :param max_range: maximum range of x and y axes
    :return:
        dataframe of certain properties regarding our graphs
    """

    graphs = create_random_graphs(max_radius, max_num_circles, num_graph, max_range)

    properties = []  # data regarding our tests
    max_radius_str = str(max_radius).replace('.', '_')  # string value of max radius

    # ploting graph
    for i in range(num_graph):
        graphs[i].colour_disc_graph()
        fig, ax = graphs[i].plot_circle_intersection_graph()
        # changing default dimensions of a plot
        if max_range is None:
            ax.set_xlim(0 - max_radius*2, max_radius * 6)
            ax.set_ylim(0 - max_radius*2, max_radius * 6)
        else:
            ax.set_xlim(0 - max_radius*2, max_range + max_radius)
            ax.set_ylim(0 - max_radius*2, max_range + max_radius)

        fig.savefig(
            f"./figures/graph_{max_radius_str}_{i}")  # saving graph to file, first max radius value and second number of graph

        properties.append([graphs[i].pseudo_chi(), graphs[i].get_Delta() + 1, graphs[i].biggest_clique(),
                           3 * graphs[i].biggest_clique() - 2, 6 * graphs[i].biggest_clique() - 6])
        df = pd.DataFrame(properties, columns=['chi', 'Delta+1', 'size of biggest clique (omega)', '3*omega-2', '6*omega-6'])
        df.to_excel(f'./dataframes/dataframe_{max_radius_str}.xlsx', index=False)  # saving our test data

    return df

def find_limits(list_of_circles):
    """
        Finds suitable limits of x and y axes for ploting graph.

    :param list_of_circles: List of Circle objects
    :return: tuple of maximum and minimum values of x and y axes
    """
    max_x = 0
    max_y = 0
    min_x = 0
    min_y = 0
    max_rad = 0
    for c in list_of_circles:
        max_x = c.pos_x if c.pos_x > max_x else max_x
        min_x = c.pos_x if c.pos_x < min_x else min_x
        max_y = c.pos_y if c.pos_y > max_y else max_y
        min_y = c.pos_y if c.pos_y < min_y else min_y
        max_rad = c.radius if c.radius > max_rad else max_rad

    return max_x + max_rad*1.5, max_y + max_rad*1.5, min_x-max_rad*1.5, min_y-max_rad*1.5

# def test_find_limits():
#     list_of_circles = [Circle(0,0,1), Circle(2,1, 2)]
#     expected_result = (5, 4, -3, -3)
#     actual_result = find_limits(list_of_circles)
#     return actual_result == expected_result


def colouring_list_test(list_of_circles, filename):
    """
        Initializes a graph from a list of circles, colours it and plots.
    Figures with graphs are in the directory figures, named {filename}.png.
    Dataframes with properties of those graphs are in the directory dataframes, named {filename}.xlsx

    :param list_of_circles: list of circles used for graph's construction
    :param filename: name of the file, that graph and dataframe is to be written to
    :return:
        dataframe with properties of this graph
    """
    g = IntersectionGraph.get_intersection_graph(list_of_circles)
    g.colour_disc_graph()
    fig, ax = g.plot_circle_intersection_graph()
    max_x, max_y , min_x, min_y = find_limits(list_of_circles)
    ax.set_xlim(min_x,  max_x)
    ax.set_ylim(min_y, max_y)
    fig.savefig(f'./figures/{filename}')
    properties = [[g.pseudo_chi(), g.get_Delta() + 1, g.biggest_clique(),
                       3 * g.biggest_clique() - 2, 6 * g.biggest_clique() - 6]]
    df = pd.DataFrame(properties, columns=['chi', 'Delta+1', 'size of biggest clique (omega)', '3*omega-2', '6*omega-6'])
    df.to_excel(f'./dataframes/{filename}.xlsx', index=False)

    return df

def main():
    # random examples
    print(colouring_test(1, 20, 5))
    print(colouring_test(5, 15, 5))
    print(colouring_test(1.5, 10, 5, 3))
    print(colouring_test(2, 15, 5))

    # test 01
    test_01 = [Circle(0, 0, 2), Circle(4, 0, 2), Circle(2, 4 * 3 ** 0.5 / 2, 2)]
    print(colouring_list_test(test_01, 'test_01'))

    # test 02
    test_02 = [Circle(0, 0, 2), Circle(4, 0, 2), Circle(4, 4, 2), Circle(0, 4, 2)]
    print(colouring_list_test(test_02, 'test_02'))

    # test 03
    test_03 = [Circle(0, 0, 1), Circle(1, 1, 1), Circle(1, -1, 1), Circle(1.45, 1.01, 1), Circle(1.45, -1.01, 1),
               Circle(2.75, 0, 1), Circle(4, 1, 1), Circle(4, -1, 1)]
    print(colouring_list_test(test_03, 'test_03'))

    # test 04
    test_04 = [Circle(0, 0, 0.5), Circle(0.5, 0, 0.7), Circle(0.75, 1.25, 1), Circle(0.75, -1.25, 1), Circle(2.75, 1.25, 1.5), Circle(2.75, -1.25, 1.5), Circle(2, 0, 0.3), Circle(3.5, 0, 0.3)]
    print(colouring_list_test(test_04, 'test_04'))

if __name__ == '__main__':
    main()
