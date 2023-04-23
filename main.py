from const import *
from geom.Circle import Circle
from graph.IntersectionGraph import IntersectionGraph


# we didn't have unit tests so let classic "print" fulfill its role
def main():
    # test 01
    test_01 = [Circle(0, 0, 2), Circle(4, 0, 2), Circle(2, 4 * 3 ** 0.5 / 2, 2)]

    # test 02
    test_02 = [Circle(0, 0, 2), Circle(4, 0, 2), Circle(4, 4, 2), Circle(0, 4, 2)]

    # test 03
    test_03 = [Circle(0, 0, 1), Circle(1, 1, 1), Circle(1, -1, 1), Circle(1.45, 1.01, 1), Circle(1.45, -1.01, 1),
               Circle(2.75, 0, 1), Circle(4, 1, 1), Circle(4, -1, 1)]

    # random example
    random_example = [Circle(rand(RANGE_FROM, RANGE_TO), rand(RANGE_FROM, RANGE_TO), RADIUS) for _ in range(AMOUNT)]

    # choices
    choices = {"01": test_01, "02": test_02, "03": test_03, "random": random_example}

    g = IntersectionGraph.get_intersection_graph(choices["03"])

    g.colour_disc_graph()
    print(g)
    g.plot_circle_intersection_graph()


if __name__ == '__main__':
    main()
