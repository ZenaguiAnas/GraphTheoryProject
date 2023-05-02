import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
# #
# # import tkinter as tk
# #
# # root = tk.Tk()
# # root.mainloop()
#
# import networkx as nx
# import matplotlib.pyplot as plt
# from tkinter import *
#
# # Create the GUI
# root = Tk()
# root.title("Graph Visualization")
#
# # Define the functions for each algorithm
# def visualize_graph1():
#     G = nx.Graph()
#     G.add_nodes_from([1, 2, 3])
#     G.add_edge(1, 2)
#     G.add_edge(2, 3)
#     G.add_edge(3, 1)
#     nx.draw(G, with_labels=True)
#     plt.show()
#
# def visualize_graph2():
#     G = nx.DiGraph()
#     G.add_nodes_from([1, 2, 3])
#     G.add_edge(1, 2)
#     G.add_edge(2, 3)
#     G.add_edge(3, 1)
#     nx.draw(G, with_labels=True)
#     plt.show()
#
# # Create the buttons
# button1 = Button(root, text="Graph 1", command=visualize_graph1)
# button1.pack()
#
# button2 = Button(root, text="Graph 2", command=visualize_graph2)
# button2.pack()
#
# # Run the GUI
# root.mainloop()


# ?

edge_list = [(1, 2), (2, 3), (3, 4), (3, 5), (4, 6), (6, 7)]

# G = nx.from_numpy_array(np.array((
#     [0, 1, 0],
#     [1, 1, 1],
#     [0, 0, 0]
# )))

G = nx.Graph()
G.add_edges_from(edge_list)
# G.add_edge(1, 2)
# G.add_edge(2, 3, weight=0.9)
# G.add_edge("A", "B")
# G.add_edge("B", "B")
# G.add_node("C")
# G.add_node(print)

# print(nx.adjacency_matrix(G))
# print(dict(G.in_degree)[7])
# print(dict(G.out_degree)[7])
print(dict(G.degree)[7])

# ? Shortest path
# print(nx.shortest_path(G, 2, 4))



# Graph complete
# G = nx.complete_graph(5)


nx.draw_spring(G, with_labels=True)
plt.show()

nx.draw_planar(G, with_labels=True)
plt.show()

# nx.draw_circular(G, with_labels=True)
# plt.show()
#
# nx.draw_shell(G, with_labels=True)
# plt.show()
#
# nx.draw_spectral(G, with_labels=True)
# plt.show()
#
# nx.draw_random(G, with_labels=True)
# plt.show()
#
# nx.draw_planar(G, with_labels=True)
# plt.show()
