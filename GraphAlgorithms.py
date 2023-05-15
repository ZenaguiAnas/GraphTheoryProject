import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def generate_graph():
    graph_type = var_graph_type.get()
    weight_type = var_weight_type.get()

    if graph_type == "Directed":
        graph = nx.DiGraph()
    else:
        graph = nx.Graph()

    lines = text_area.get("1.0", tk.END).strip().split("\n")
    for line in lines:
        node1, node2 = line.strip().split()

        if weight_type == "Weighted":
            graph.add_edge(node1, node2, weight=1)
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

window = tk.Tk()
window.title("Graph Algorithm GUI")

var_graph_type = tk.StringVar(value="Directed")

graph_type_frame = tk.LabelFrame(window, text="Graph Type")
graph_type_frame.pack(padx=10, pady=10)

directed_radio = tk.Radiobutton(graph_type_frame, text="Directed", variable=var_graph_type, value="Directed")
directed_radio.pack(anchor=tk.W)

undirected_radio = tk.Radiobutton(graph_type_frame, text="Undirected", variable=var_graph_type, value="Undirected")
undirected_radio.pack(anchor=tk.W)

var_weight_type = tk.StringVar(value="Unweighted")

weight_type_frame = tk.LabelFrame(window, text="Weight Type")
weight_type_frame.pack(padx=10, pady=10)

weighted_radio = tk.Radiobutton(weight_type_frame, text="Weighted", variable=var_weight_type, value="Weighted")
weighted_radio.pack(anchor=tk.W)

unweighted_radio = tk.Radiobutton(weight_type_frame, text="Unweighted", variable=var_weight_type, value="Unweighted")
unweighted_radio.pack(anchor=tk.W)

text_area_frame = tk.LabelFrame(window, text="Nodes")
text_area_frame.pack(padx=10, pady=10)

text_area = tk.Text(text_area_frame, width=30, height=10)
text_area.pack()

generate_button = tk.Button(window, text="Generate Graph", command=generate_graph)
generate_button.pack(pady=10)

canvas_frame = tk.Frame(window)
canvas_frame.pack(padx=10, pady=10)

window.mainloop()
