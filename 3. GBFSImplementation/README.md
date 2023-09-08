# Solving the 8-Puzzle Problem using Greedy Best-First Search (GBFS)

## Introduction
The 8-Puzzle is a popular sliding puzzle that consists of a 3x3 grid with eight numbered tiles and one blank space. The goal of the puzzle is to rearrange the tiles to achieve a specific target configuration. The puzzle starts with a random initial state, and the player or an algorithm must find a sequence of moves to reach the goal state.

In this document, we will describe the 8-Puzzle problem and demonstrate how to solve it using Python code that employs Greedy Best-First Search (GBFS) with a heuristic function based on the Manhattan distance.

## The 8-Puzzle Problem

### Problem Definition
The 8-Puzzle problem is defined as follows:

- Given an initial state of the 8-Puzzle, consisting of a 3x3 grid with numbers from 1 to 8 and one blank space, and a target or goal state.
- The objective is to move the tiles in the initial state to reach the goal state through a sequence of moves.
- Only one tile can be moved at a time into the adjacent empty space (up, down, left, or right).
- The goal state is typically a predefined configuration where the tiles are ordered from left to right and top to bottom, with the blank space at the bottom-right corner.

### Example:
Here is an example of an initial state and a goal state:

**Initial State:**
```
1 2 3
8 0 4
7 6 5
```

**Goal State:**
```
1 2 3
8 0 4
7 6 5
```

The task is to find a sequence of moves that transforms the initial state into the goal state.

## Solving the 8-Puzzle using Greedy Best-First Search (GBFS)

### Overview
Greedy Best-First Search (GBFS) is an informed search algorithm that uses a heuristic function to guide the search towards the goal. In the context of the 8-Puzzle, GBFS calculates a heuristic value for each state (node) in the search tree based on how close the state is to the goal state, using a heuristic called the Manhattan distance.

The key components of the Python code for solving the 8-Puzzle using GBFS are as follows:

- A `PuzzleState` class represents a state of the puzzle. It includes methods for generating successor states, calculating the Manhattan distance heuristic, and comparing states.
- The `gbfs` function performs the Greedy Best-First Search, exploring states in a priority queue based on their heuristic values.
- The `read_input` function reads the initial state of the puzzle from a text file.
- The program accepts a command-line argument specifying the input file containing the initial state and attempts to find a solution.

### Implementation
Below is the Python code for solving the 8-Puzzle problem using Greedy Best-First Search (GBFS), along with explanations for key parts of the code:

```python
import heapq  # Import the 'heapq' module for implementing a priority queue
from collections import deque  # Import the 'deque' class for implementing a queue

# Define a class to represent a state of the puzzle
class PuzzleState:
    def __init__(self, state, parent=None, action=None):
        self.state = state  # The current state of the puzzle
        self.parent = parent  # The parent state that led to this state
        self.action = action  # The action (row, column) taken to reach this state

    def __eq__(self, other):
        return self.state == other.state  # Compare the states of two PuzzleState objects

    def __hash__(self):
        return hash(str(self.state))  # Calculate the hash value based on the string representation of the state

    def get_blank_position(self):
        for i, row in enumerate(self.state):  # Iterate through each row of the state
            if 0 in row:  # If 0 (blank tile) is found in the row
                return i, row.index(0)  # Return the row and column indices of the blank tile
    
    def generate_successors(self):
        successors = []  # List to store generated successor states
        blank_row, blank_col = self.get_blank_position()  # Get the current position of the blank tile

        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Define possible moves: (down, up, right, left)

        for dr, dc in moves:
            new_row, new_col = blank_row + dr, blank_col + dc  # Calculate the new position after the move

            if 0 <= new_row < 3 and 0 <= new_col < 3:  # Check if the new position is within the puzzle boundaries
                new_state = [row[:] for row in self.state]  # Create a copy of the current state
                new_state[blank_row][blank_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_row][blank_col]  # Perform the swap
                successors.append(PuzzleState(new_state, self, (blank_row, blank_col)))  # Append the generated successor state

        return successors  # Return the list of generated successor states

    def h(self, goal_state):
        # Define a heuristic function (Manhattan distance) to estimate the cost to reach the goal
        cost = 0
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != 0:
                    goal_row, goal_col = divmod(self.state[i][j] - 1, 3)
                    cost += abs(i - goal_row) + abs(j - goal_col)
        return cost

    def f(self, goal_state):
        # The cost function for GBFS is just the heuristic value
        return self.h(goal_state)

    def __lt__(self, other):
        # Define the less-than comparison for ordering in the priority queue
        return self.f(goal_state) < other.f(goal_state)
```

**Explanation:**
- `PuzzleState` class: Represents a state of the 8-Puzzle. It includes methods for comparing states, calculating a heuristic value, generating successor states, and defining the less-than comparison for ordering in the priority queue.

```python
# Declare global variable explored_states
explored_states = 0
```

**Explanation:** This variable keeps track of the total number of states explored during the search process.

```python
# Define the Greedy Best-First Search (GBFS) function
def gbfs(initial_state, goal_state):
    global explored_states
    visited = set()  # Set to store visited states
    priority_queue = []  # Priority queue to store states to be explored

    # We'll use a tuple (priority, state) for the priority queue
    heapq.heappush(priority_queue, (initial_state.f(goal_state), initial_state))
```

**Explanation:**
- `gbfs` function: Performs the Greedy Best-First Search. It initializes data structures, including a priority queue, to store states for exploration.

```python
    while priority_queue:
        _, current_state = heapq.heappop(priority_queue)  # Get the current state from the priority queue
        visited.add(current_state)  # Mark the current state as visited
        explored_states += 1  # Increment the counter for explored states

        if current_state.state == goal_state:  # If the current state matches the goal state
            path = []
            while current_state:
                path.append(current_state.state)
                current_state = current_state.parent
            return list(reversed(path))  # Return the reversed path from the initial state to the goal state

        successors = current_state.generate_successors()  # Generate successor states
        for successor in successors:
            if successor not in visited:  # If the successor state hasn't been visited
                heapq.heappush(priority_queue, (successor.f(goal_state), successor))  # Add the successor to the priority queue for exploration
```

**Explanation:**
- The while loop iteratively explores states in the priority queue until the goal state is reached or no solution is found.
- It uses a priority queue to select states with lower heuristic values first.
- The heuristic value is calculated using the Manhattan distance heuristic.
- If the goal state is found, it reconstructs the path from the goal state to the initial state and returns it.
- Successor states are generated and added to the priority queue for further exploration.

```python
    return None  # Return None if no solution is found
```

**Explanation:** If the while loop completes without finding a solution, the function returns `None` to indicate that no solution was found.

The rest of the code includes functions for reading the input from a text file and the main part of the script that accepts the input file and calls the `gbfs` function to solve the 8-Puzzle problem.

I hope these explanations help you understand how the code works to solve the 8-Puzzle problem using Greedy Best-First Search (GBFS) with a heuristic function based on the Manhattan distance.

### Usage
To use the provided Python code to solve the 8-Puzzle problem, follow these steps:

1. Create a text file containing the initial state of the puzzle, with numbers from 0 to 8 arranged in a 3x3 grid, where 0 represents the blank space.
   Example:
   ```
   1 2 3
   8 0 4
   7 6 5
   ```
2. Save the file and note its path.

3. Open a terminal or command prompt.

4. Run the Python script with the following command, providing the path to the text file as a command-line argument:
   ```
   python GBFS.py filename.txt
   ```
   Replace `filename.txt` with the actual path to your input file.

5. The program will attempt to find a solution to the 8-Puzzle problem using Greedy Best-First Search (GBFS) with the Manhattan distance heuristic. If a solution is found, it will display the steps to reach the goal state. Otherwise, it will indicate that no solution was found.

6. The total number of explored states will also be displayed, indicating the efficiency of the search process.

### Example
Suppose you have an input file named `puzzle.txt` containing the following initial state:

```
1 2 3
8 0 4
7 6 5
```

You can solve the puzzle by running the following command:

```
python GBFS.py puzzle.txt
```

The program will display the steps to solve the puzzle and the total number of explored states.

## Conclusion
The 8-Puzzle problem is a classic puzzle that can be solved efficiently using search algorithms such as Greedy Best-First Search (GBFS) with appropriate heuristic functions. The provided Python code demonstrates how to solve the 8-Puzzle problem using GBFS and a Manhattan distance heuristic. By following the steps outlined in this document, you can solve 8-Puzzle instances of your own and gain a better understanding of search algorithms and heuristic functions.