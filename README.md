DrinkTree

DrinkTree is an interactive beverage recommendation system based on a decision flow. The project was developed in Python with the main objective of demonstrating, in a practical and integrated way, the application of three fundamental concepts of Computer Science: Data Structures (Binary Trees), Object-Oriented Programming (OOP), and Recursive Algorithms.

Concepts Demonstrated

- Binary Tree: All decision-making is structured in nodes. Each question has exactly two possible branches: `yes` or `no`, which guide the user to the leaves of the tree (the drinks).

- Object-Oriented Programming: Clear division of responsibilities through classes. The `Menu` class acts as the template for our data nodes, while the `ExpertSuggestor` class encapsulates the logic of behavior and management of the tree.

- Recursion: Instead of using traditional repetition structures (`while` or `for`), the system navigates, counts elements, and renders the tree using self-calling functions, relying on well-defined "base cases" to avoid infinite loops.

Code Features

The main file `DrinkTree.py` has three main orchestrating methods:
1. `suggest()`: The recommendation engine. Asks binary questions in the terminal and recursively advances through the nodes depending on the user's answer.

2. `drinksCount()`: An algorithmic counter that recursively traverses all the leaves of the tree to return the exact number of drinks available on the menu.

3. `showTree()`: A visualization tool that prints the entire tree structure to the terminal, using visual indents proportional to the depth level of each node.

Prerequisites and How to Run:

- Python installed on your machine (version 3.x recommended).
