**8-Puzzle Problem**

The 8-Puzzle is a classic sliding puzzle game that consists of a 3x3 grid with eight numbered tiles and an empty space (represented as "0"). The goal of the game is to rearrange the tiles from their initial configuration to a target or goal configuration, typically arranged in ascending order. The puzzle is solved when all tiles are in the correct order, and the empty space is in a specific location (usually the bottom-right corner).

**Solving the 8-Puzzle Problem using A* Search**

The A* (A-star) search algorithm is a widely used technique for solving problems like the 8-Puzzle. It combines the advantages of both Dijkstra's algorithm (finding the shortest path) and greedy best-first search (using a heuristic to estimate the remaining cost). A* uses a priority queue to explore the most promising states first.

**Explanation of the Provided Code**

Here's a detailed explanation of the Python code provided for solving the 8-Puzzle problem using the A* search algorithm:

1. **PuzzleState Class**:
    - This class represents the state of the puzzle at any given time.
    - It includes the current state, a reference to the parent state, and the action (move) that led to the current state.
    - The `g` attribute stores the cost from the initial state to the current state.
    - The `__eq__` method compares two `PuzzleState` objects by comparing their states.
    - The `__hash__` method computes a hash value based on the string representation of the state.
    - `get_blank_position` finds the row and column of the blank tile (0).
    - `generate_successors` generates possible successor states by moving the blank tile in all valid directions.
    - `h` calculates a heuristic estimate (Manhattan distance) of the cost to reach the goal state from the current state.
    - `f` computes the evaluation function, which is the sum of the actual cost (`g`) and the heuristic value (`h`).
    - `__lt__` defines the less-than comparison, used for ordering in the priority queue.

2. **Global Variables**:
    - `explored_states` keeps track of the total number of states explored during the search.

3. **A* Search Algorithm (`astar` function)**:
    - It takes the initial state and the goal state as input.
    - `visited` is a set to store visited states.
    - `priority_queue` is a priority queue (min-heap) to store states to be explored.
    - States in the priority queue are ordered by their evaluation function values (`f`).
    - The algorithm iteratively explores states until the goal state is reached or no solution is found.
    - For each state, successors are generated and added to the priority queue if they have not been visited.
    - The cost `g` is updated for each successor.
    - The algorithm returns the solution path (a sequence of states) if a solution is found; otherwise, it returns `None`.

4. **Reading Input (`read_input` function)**:
    - Reads the initial state of the puzzle from a text file.
    - The file should contain three lines, each with three numbers separated by spaces, representing the initial state of the 8-Puzzle.

5. **Main Execution**:
    - Checks the command-line arguments for the input filename.
    - Reads the initial state and sets the goal state.
    - Calls the `astar` function to solve the puzzle.
    - If a solution is found, it prints each step of the solution path.
    - If no solution is found, it prints a message indicating that.
    - Finally, it displays the total number of states explored during the search.

This code efficiently uses the A* search algorithm and heuristic to solve the 8-Puzzle problem and provides step-by-step output to visualize the solution path. You can run this code by providing the filename of an input file containing the initial state of the puzzle as a command-line argument.