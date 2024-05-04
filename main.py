import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random

seed = 0
random.seed(seed)
np.random.seed(seed)


def main():
    graphe = nx.Graph()
    graphe.add_node('A')
    graphe.add_node('B')
    graphe.add_node('C')
    graphe.add_node('D')
    graphe.add_node('E')

    #graphe.add_edge()

    nx.draw(graphe, with_labels=True, node_color='Green', node_size=3000, font_size=20, font_family='Times New Roman')
    plt.margins(0.2)
    plt.show()


if __name__ == '__main__':
    main()

