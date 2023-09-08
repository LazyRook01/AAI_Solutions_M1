Here we define a puzzle-solving program using Depth-First Search (DFS). The puzzle in question is a classic 8-puzzle, which consists of a 3x3 grid with eight numbered tiles and one empty space, arranged in a scrambled initial state. The goal is to reach a specified target state by sliding the tiles into the empty space.

Here's a detailed explanation of the code:

1. **PuzzleState Class**: This class is used to represent a state of the puzzle. Each state contains the current arrangement of tiles, a reference to its parent state (the state that led to this one), and the action (row, column) taken to reach this state.

   - `__init__(self, state, parent=None, action=None)`: Initializes a PuzzleState object with the given state, parent state (defaulting to None), and action (defaulting to None).

   - `__eq__(self, other)`: Defines how two PuzzleState objects are considered equal by comparing their states.

   - `__hash__(self)`: Calculates the hash value of a PuzzleState based on its string representation.

   - `get_blank_position(self)`: Finds the position (row and column) of the blank tile (represented as 0) in the puzzle grid.

   - `generate_successors(self)`: Generates a list of successor states by considering possible moves (up, down, left, and right) of the blank tile. It creates new states by swapping the blank tile with adjacent tiles and returns the list of successor states.

2. **Global Variables**:
   - `explored_states`: A global variable to keep track of the number of explored states during the DFS search.

3. **DFS Function**:
   - `dfs(initial_state, goal_state)`: This function performs Depth-First Search to find a solution to the puzzle.

     - `visited`: A set to keep track of visited states to avoid revisiting the same state.

     - `stack`: A stack data structure to store states to be explored. It starts with the initial state.

     - The while loop continues until the stack is empty, meaning all possible states have been explored.

     - For each iteration of the loop:
       - Pop the top state from the stack.
       - Mark the state as visited.
       - Increment the `explored_states` counter.

     - Check if the current state matches the goal state. If so, reconstruct and return the path from the initial state to the goal state.

     - Generate successor states for the current state using the `generate_successors` method of the `PuzzleState` class.

     - Add unvisited successor states to the stack for exploration.

4. **Input Reading Function**:
   - `read_input(filename)`: This function reads the initial state of the puzzle and the predefined goal state from an input file.

     - It opens the specified file and reads the first three lines to extract the initial state, parsing it into a 2D list.

5. **Main Execution Block**:
   - The program checks if it is being run as the main script (`if __name__ == '__main__':`).

   - It checks if the correct number of command-line arguments (the input filename) is provided and exits with an error message if not.

   - It reads the initial state and goal state from the input file using the `read_input` function.

   - It calls the `dfs` function to find a solution to the puzzle.

   - If a solution is found, it prints each step of the solution, including the state and the total number of states explored.

   - If no solution is found, it prints a message indicating this.

The code is organized to solve the 8-puzzle problem by searching for a path from the initial state to the goal state using Depth-First Search. It uses a `PuzzleState` class to represent and manipulate states of the puzzle and employs a stack to manage the search process.