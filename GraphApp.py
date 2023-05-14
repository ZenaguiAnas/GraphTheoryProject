import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt

class GraphApp:

    def __init__(self, master):
        self.master = master
        master.title("Graph Visualization App")

        # Create the matrix input field
        self.matrix_label = tk.Label(master, text="Matrix:")
        self.matrix_label.grid(row=0, column=0)
        self.matrix_field = tk.Text(master, height=5, width=40)
        self.matrix_field.grid(row=0, column=1)

        # Create the algorithm input field
        self.algorithm_label = tk.Label(master, text="Algorithm:")
        self.algorithm_label.grid(row=1, column=0)
        self.algorithm_field = tk.Entry(master)
        self.algorithm_field.grid(row=1, column=1)

        # Create the directed checkbox
        self.directed_var = tk.BooleanVar()
        self.directed_checkbox = tk.Checkbutton(master, text="Directed", variable=self.directed_var)
        self.directed_checkbox.grid(row=2, column=0)

        # Create the visualize button
        self.visualize_button = tk.Button(master, text="Visualize", command=self.visualize)
        self.visualize_button.grid(row=3, column=0)

    def visualize(self):
        # Get the input values
        matrix = self.matrix_field.get("1.0", tk.END).strip()
        algorithm = self.algorithm_field.get()
        directed = self.directed_var.get()

        # Parse the matrix input
        matrix = [list(map(int, row.split())) for row in matrix.split("\n")]

        # Create a Networkx graph object
        G = nx.DiGraph() if directed else nx.Graph()

        # Add the nodes to the graph
        for i in range(len(matrix)):
            G.add_node(i)

        # Add the edges to the graph
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] != 0:
                    G.add_edge(i, j)

        # Visualize the graph
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True)
        plt.show()

root = tk.Tk()
app = GraphApp(root)
root.mainloop()
