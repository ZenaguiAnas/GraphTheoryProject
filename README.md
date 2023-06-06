# graphTheoryProject

# **Graph Algorithm GUI Documentation**

****This documentation provides an overview of the code for the Graph Algorithm GUI implemented using the tkinter library in Python. The GUI allows users to generate graphs, visualize them, and run various graph algorithms such as Breadth-First Search (BFS), Depth-First Search (DFS), and Dijkstra's algorithm.

## Dependencies

The code requires the following Python libraries to be installed:

- **`tkinter`:** The standard Python interface to the Tk GUI toolkit.
- **`networkx`:** A library for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks.
- **`matplotlib`:** A plotting library for creating static, animated, and interactive visualizations in Python.

## Code Structure

The code is structured as follows:

1. **Importing the required libraries:**
    - **`tkinter`** as **`tk:`** Used for creating the GUI.
    - **`networkx`** as **`nx`**: Used for graph creation and algorithm implementation.
    - **`matplotlib.pyplot`** as **`plt`**: Used for graph visualization.
    - **`FigureCanvasTkAgg`** from **`matplotlib.backends.backend_tkagg`**: Used to embed matplotlib figures in Tkinter GUI.
    - **`ttk`** from **`tkinter`**: Used for creating themed widgets.
2. **Defining the functions:**
    - **`run_algorithm(algorithm)`**: Executes the selected graph algorithm (BFS, DFS, or Dijkstra) on the generated graph.
    - **`generate_graph()`**: Parses the user input from the text area, generates the graph based on the input, and visualizes it.
3. **Creating the GUI:**
    - Creating the main Tkinter window.
    - Defining the variables and options for graph type (directed/undirected) and weight type (weighted/unweighted).
    - Creating frames and widgets for graph type selection, weight type selection, algorithm selection, start node selection, text area input, generate button, canvas for visualization, and result label.
    - Setting up event handlers for the algorithm buttons and the generate button.
    - Running the Tkinter event loop.
    

## Usage

To use the Graph Algorithm GUI, follow these steps:

1. Make sure you have all the required dependencies installed (**`tkinter`**, **`networkx`**, **`matplotlib`**).
2. Run the Python script.
3. The GUI window will appear with the following sections and controls:
    - **`Graph Type`**: Select whether the graph is directed or undirected.
    - **`Weight Type`**: Select whether the graph edges have weights or not.
    - **`Algorithms`**: Buttons to run BFS, DFS, or Dijkstra's algorithm.
    - **`Start Node`**: Select the starting node for the algorithms.
    - **`Nodes (Node1 Node2 [Weight])`**: Enter the graph nodes and edges. Optionally, provide the weight for each edge if the weight type is selected as "Weighted".
    - **`Generate Graph`**: Click this button to generate and visualize the graph based on the provided input.
    - **`Visualization`**: The generated graph will be displayed in this area.
    - **`Results`**: The results of the executed algorithms will be displayed here.

1. Select the graph type (directed/undirected) and weight type (weighted/unweighted) according to your requirements.
2. Enter the nodes and edges in the text area. Each line should represent an edge in the format: "Node1 Node2 [Weight]". If the weight type is selected as "Weighted", provide the weight for each edge.
3. Click the **`Generate Graph`** button to generate and visualize the graph based on the input.
4. Select one of the algorithm buttons (**`BFS`**, **`DFS`**, or **`Dijkstra`**) to execute the corresponding algorithm on the generated graph. The results will be displayed in the **`Results`** area.

## Notes

📌 The code utilizes the **`networkx`** library for graph creation and algorithm implementation, and matplotlib for graph visualization. Make sure these libraries are installed before running the code.

📌 The GUI provides options for selecting graph types, weight types, and algorithms. Users can input graph nodes and edges to generate custom graphs.
📌 The graph visualization is displayed using the **`matplotlib`** library embedded in the **`Tkinter`** GUI window.
📌 The algorithm results are shown in the GUI's result label.
📌 Proper error handling and validation are implemented to handle various scenarios such as empty input, missing start node, and missing weights for weighted graphs.

This concludes the documentation for the Graph Algorithm GUI code. You can use this documentation as a reference to understand the code's structure and functionality.
