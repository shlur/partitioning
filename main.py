import pymetis
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
# from scipy import sparse
from scipy.sparse import csr_matrix
from numpy import genfromtxt
import math


# adjacency_matrix = genfromtxt('matrix.csv', delimiter=',')
#
# for i in range(0, len(adjacency_matrix)):
#     for j in range(0, len(adjacency_matrix)):
#         if adjacency_matrix[i][j] != 0:
#             adjacency_matrix[i][j] = int(adjacency_matrix[i][j])
#         if j >= i:
#             adjacency_matrix[i][j] = None
#
#
# print(adjacency_matrix)
#
# print(len(adjacency_matrix))

adjacency_matrix = np.matrix([[0, 0, 0, 0, 0, 0],
                              [1, 0, 0, 0, 0, 0],
                              [1, 1, 0, 0, 0, 0],
                              [0, 1, 0, 0, 0, 0],
                              [0, 1, 1, 1, 0, 0],
                              [0, 1, 1, 1, 1, 1]])


parts = 3

sprs = csr_matrix(adjacency_matrix)
# , dtype=np.uint8

print(sprs.indices.tolist())
print(len(sprs.indices.tolist()))
print(sprs.data)
print(len(sprs.data))


partition = pymetis.part_graph(int(parts), xadj=(sprs.indptr.tolist()), adjncy=(sprs.indices.tolist()))[1]

print(partition)
#
# G = nx.Graph()
# for i in range(0, len(adjacency_list))print(sprs.data):
#     G.add_edge(adjacency_list[i][0], adjacency_list[i][1])
#     print(adjacency_list[i][0], adjacency_list[i][1])

colors = ['red', 'blue', 'green', 'yellow', 'darkslateblue', 'brown', 'grey', 'cornflowerblue', 'pink', 'orange']
node_color = []


G = nx.from_numpy_matrix(adjacency_matrix)

for i, p in enumerate(partition):
    print(i, colors[p])
    G.node[i]['color'] = colors[p]
    node_color.append(G.node[i]['color'])


nx.draw(G, node_color=node_color, with_labels=True)

plt.show()