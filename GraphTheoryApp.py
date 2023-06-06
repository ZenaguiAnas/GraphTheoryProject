import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk
from tkinter import messagebox


def run_algorithm(algorithm):
    start_node = start_node_var.get()

    if not graph:
        messagebox.showerror("Error", "Please generate a graph first.")
        return

    if not start_node:
        messagebox.showerror("Error", "Please select a start node.")
        return

    results_label.config(text="")

    if algorithm == "BFS":
        bfs_result = list(nx.bfs_tree(graph, start_node))
        results_label.config(text=f"BFS Result: {bfs_result}")
    elif algorithm == "DFS":
        dfs_result = list(nx.dfs_tree(graph, start_node))
        results_label.config(text=f"DFS Result: {dfs_result}")
    elif algorithm == "Dijkstra":
        dijkstra_result = nx.single_source_dijkstra(graph, start_node)
        results_label.config(text=f"Dijkstra Result: {dijkstra_result[0]}")


def generate_graph():
    global graph
    graph_type = var_graph_type.get()
    weight_type = var_weight_type.get()

    if graph_type == "Directed":
        graph = nx.DiGraph()
    else:
        graph = nx.Graph()

    lines = text_area.get("1.0", tk.END).strip().split("\n")
    for line in lines:
        items = line.strip().split()
        node1, node2 = items[:2]

        if weight_type == "Weighted":
            if len(items) > 2:
                weight = float(items[2])
                graph.add_edge(node1, node2, weight=weight)
            else:
                messagebox.showerror("Error", "Please enter weights for all edges.")
                return
        else:
            graph.add_edge(node1, node2)

    pos = nx.spring_layout(graph)
    plt.figure()
    if weight_type == "Weighted":
        nx.draw_networkx(graph, pos, with_labels=True, arrows=True)
        labels = nx.get_edge_attributes(graph, 'weight')
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    else:
        nx.draw_networkx(graph, pos, with_labels=True, arrows=True)

    canvas = FigureCanvasTkAgg(plt.gcf(), master=canvas_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

    nodes = list(graph.nodes())
    start_node_select['values'] = nodes


window = tk.Tk()
window.title("Graph Algorithm GUI")

var_graph_type = tk.StringVar(value="Directed")

graph_type_frame = tk.LabelFrame(window, text="Graph Type")
graph_type_frame.pack(padx=10, pady=10, side="left")

directed_radio = tk.Radiobutton(graph_type_frame, text="Directed", variable=var_graph_type, value="Directed")
directed_radio.pack(anchor=tk.W)

undirected_radio = tk.Radiobutton(graph_type_frame, text="Undirected", variable=var_graph_type, value="Undirected")
undirected_radio.pack(anchor=tk.W)

var_weight_type = tk.StringVar(value="Unweighted")

weight_type_frame = tk.LabelFrame(window, text="Weight Type")
weight_type_frame.pack(padx=10, pady=10, side="left")

weighted_radio = tk.Radiobutton(weight_type_frame, text="Weighted", variable=var_weight_type, value="Weighted")
weighted_radio.pack(anchor=tk.W)

unweighted_radio = tk.Radiobutton(weight_type_frame, text="Unweighted", variable=var_weight_type, value="Unweighted")
unweighted_radio.pack(anchor=tk.W)

algorithm_frame = ttk.LabelFrame(window, text="Algorithms")
algorithm_frame.pack(padx=10, pady=10, side="left")

bfs_button = ttk.Button(algorithm_frame, text="BFS", command=lambda: run_algorithm("BFS"))
bfs_button.pack(pady=5)

dfs_button = ttk.Button(algorithm_frame, text="DFS", command=lambda: run_algorithm("DFS"))
dfs_button.pack(pady=5)

dijkstra_button = ttk.Button(algorithm_frame, text="Dijkstra", command=lambda: run_algorithm("Dijkstra"))
dijkstra_button.pack(pady=5)

start_node_frame = ttk.LabelFrame(window, text="Start Node")
start_node_frame.pack(padx=10, pady=10, side="right")

start_node_var = tk.StringVar()
start_node_select = ttk.Combobox(start_node_frame, textvariable=start_node_var)
start_node_select.pack()

text_area_frame = tk.LabelFrame(window, text="Nodes (Node1 Node2 [Weight])")
text_area_frame.pack(padx=10, pady=10)

text_area = tk.Text(text_area_frame, width=30, height=10)
text_area.pack()

generate_button = ttk.Button(window, text="Generate Graph", command=generate_graph)
generate_button.pack(pady=10)

canvas_frame = tk.Frame(window)
canvas_frame.pack(padx=10, pady=10)

results_label = ttk.Label(window, text="")
results_label.pack(pady=10)

window.mainloop()

