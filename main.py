import random

import pandas as pd

from const import *
from geom.Circle import Circle
from graph.IntersectionGraph import IntersectionGraph


def test_colouring(max_radius, max_num_circles, num_graph, max_range=None):
    """
        tests colouring of intersection graphs, returns maximum degree
        and number of colours used
    :param max_radius: maximum radius of circles, should not be smaller 0.5
    :param max_num_circles: how many circles are supposed to be initiated
    :param num_graph: how many graphs do we want to test
    :param max_range: maximum range of x and y axes
    :return:
        dataframe of certain properties regarding our graphs
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

    properties = []  # data regarding our tests
    max_radius_str = str(max_radius).replace('.', '_')  # string value of max radius

    # ploting graph
    for i in range(num_graph):
        graphs[i].colour_disc_graph()
        fig, ax = graphs[i].plot_circle_intersection_graph()
        if max_range is None:
            ax.set_xlim(0 - max_radius, max_radius * 6)
            ax.set_ylim(0 - max_radius, max_radius * 6)
        else:
            ax.set_xlim(0 - max_radius, max_range + max_radius)
            ax.set_ylim(0 - max_radius, max_range + max_radius)

        fig.savefig(f"./figures/graph_{max_radius_str}_{i}") # saving graph to file, first max radius value and second number of graph

        properties.append([graphs[i].pseudo_chi(), graphs[i].get_Delta() + 1, graphs[i].biggest_clique(),
                           3 * graphs[i].biggest_clique() - 2])
        df = pd.DataFrame(properties, columns=['chi', 'Delta+1', 'size of biggest clique (omega)', '3*omega-2'])
        df.to_excel(f'./dataframes/dataframe_{max_radius_str}.xlsx', index=False) # saving our test data
    return df


def main():
    print(test_colouring(1, 20, 5))
    print(test_colouring(5, 15, 5))
    print(test_colouring(1.5, 10, 5, 2))
    print(test_colouring(2, 15, 5))

    # import matplotlib.pyplot as plt
    # import numpy as np
    #
    # # Define a list of 20 colors
    # colors = plt.cm.tab20(np.linspace(0, 1, 20))
    #
    # # Print the colors
    # print(colors)

    # # test 01
    # test_01 = [Circle(0, 0, 2), Circle(4, 0, 2), Circle(2, 4 * 3 ** 0.5 / 2, 2)]
    #
    # # test 02
    # test_02 = [Circle(0, 0, 2), Circle(4, 0, 2), Circle(4, 4, 2), Circle(0, 4, 2)]
    #
    # # test 03
    # test_03 = [Circle(0, 0, 1), Circle(1, 1, 1), Circle(1, -1, 1), Circle(1.45, 1.01, 1), Circle(1.45, -1.01, 1),
    #            Circle(2.75, 0, 1), Circle(4, 1, 1), Circle(4, -1, 1)]
    #
    # # random example
    # random_example = [Circle(rand(RANGE_FROM, RANGE_TO), rand(RANGE_FROM, RANGE_TO), RADIUS) for _ in range(AMOUNT)]
    #
    # # choices
    # choices = {"01": test_01, "02": test_02, "03": test_03, "random": random_example}
    #
    # g = IntersectionGraph.get_intersection_graph(choices["03"])
    #
    # g.colour_disc_graph()
    # print(g)
    # g.plot_circle_intersection_graph()


if __name__ == '__main__':
    main()
