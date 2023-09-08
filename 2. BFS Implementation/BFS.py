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


# Declare global variable explored_states
explored_states = 0

# Define the Breadth-First Search (BFS) function
def bfs(initial_state, goal_state):
    global explored_states
    visited = set()  # Set to store visited states
    queue = deque([PuzzleState(initial_state)])  # Queue to store states to be explored

    while queue:
        current_state = queue.popleft()  # Get the current state from the front of the queue
        visited.add(current_state)  # Mark the current state as visited
        explored_states += 1  # Increment the counter for explored states

        if current_state.state == goal_state:  # If the current state matches the goal state
            path = []
            while current_state:
                path.append(current_state.state)
                current_state = current_state.parent
            return list(reversed(path))  # Return the reversed path from initial state to goal state

        successors = current_state.generate_successors()  # Generate successor states
        for successor in successors:
            if successor not in visited:  # If the successor state hasn't been visited
                queue.append(successor)  # Add the successor to the queue for exploration

    return None  # Return None if no solution is found


# Define a function to read the input from a file
def read_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()  # Read all lines from the file

    initial_state = [[int(num) if num != ' ' else 0 for num in line.strip()] for line in lines[:3]]  # Extract the initial state from the first 3 lines of the file
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]  # Define the goal state

    return initial_state, goal_state  # Return the initial and goal states as a tuple


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 2:
        print("Usage: python m1.py filename.txt")  # Print usage instructions if the command line argument is missing or incorrect
        sys.exit(1)  # Exit with an error code

    input_filename = sys.argv[1]  # Get the input filename from the command line argument
    initial_state, goal_state = read_input(input_filename)  # Read the initial and goal states from the input file

    solution = bfs(initial_state, goal_state)  # Solve the puzzle using BFS
    if solution:
        for step, state in enumerate(solution):
            print(f"Step {step}:\n")
            for row in state:
                print(" ".join(map(str, row)))  # Print each step of the solution
            print("\n")
    else:
        print("No solution found.")  # Print a message if no solution is found
    
    print("Total states explored:", explored_states)  # Print the total number of explored states
