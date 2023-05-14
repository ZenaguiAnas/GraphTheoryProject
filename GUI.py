import tkinter as tk
from tkinter import ttk
from tkinter import *

window = tk.Tk()
window.title("Graph Application")
window.geometry("800x800")

# label = tk.Label(window, text="Graph", padx=20, pady=20)
# # label.grid(row=0, column=0)
# label.grid(row=0, column=0, columnspan=2)
#
# username_entry = tk.Entry(window)
# username_entry.grid(row=0, column=2)

frame = tk.Frame(window)
frame.pack(pady=20)

labelOfFrame = tk.LabelFrame(frame, text="Data input", padx=30, pady=30)
labelOfFrame.grid(row=0, column=0)

matrixLabel = tk.Label(labelOfFrame, text="Matrix")
matrixLabel.grid(row=1, column=0)

matrixInput = tk.Text(labelOfFrame, width=5, height=5, padx=40)
matrixInput.grid(row=1, column=1)

graphTypeFrame = tk.LabelFrame(frame, text="Graph Type", padx=30)
graphTypeFrame.grid(row=0, column=3)

radioboxTitle = tk.Radiobutton(graphTypeFrame, text="Directed")
radioboxTitle.grid(row=1, column=3)

radioboxTitle = tk.Radiobutton(graphTypeFrame, text="Undirected")
radioboxTitle.grid(row=2, column=3)

submitButton = tk.Button(labelOfFrame, text="Generate")
submitButton.grid(row=1, column=4, padx=30)

graphFormTitle = tk.Label(window, text="Graph Representation")
graphFormTitle.pack(pady=20)
graphForm = Canvas(window, width=500, height=350, bg="white")
graphForm.pack()

AlgorithmsFrame = tk.Frame(window)
AlgorithmsFrame.pack(pady=20)

algorithmesTitle = Label(AlgorithmsFrame, text="Choose an Algorithm")
algorithmesTitle.grid(row=0, column=1, padx=30)

algorithmes_combobox = ttk.Combobox(AlgorithmsFrame, values=["Kruskal", "BFS", "DFS"])
algorithmes_combobox.grid(row=1, column=1, padx=30)

calculateButton = tk.Button(AlgorithmsFrame, text="Generate")
calculateButton.grid(row=1, column=3, padx=30)




window.mainloop()



