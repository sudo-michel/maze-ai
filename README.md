# Maze Generator and Solver

This Python program generates a random maze and solves it using two different algorithms: Depth-First Search (DFS) and A\*. The maze is displayed using Pygame, and the paths found by the algorithms are visualized.

## Features

- Generates a random maze with specified width and height.
- Solves the maze using Depth-First Search (DFS).
- Solves the maze using A\* algorithm.
- Visualizes the maze and the paths found by DFS and A\* using Pygame.

## Requirements

- Python 3.x
- Pygame library

You can install Pygame using pip:

```bash
pip install pygame
```

## Usage

1. Clone the repository or download the script.
2. Run the script using Python:

```bash
python maze_solver.py
```

3. The program will generate a maze, solve it using DFS and A\*, and display the results in a Pygame window.

## Code Explanation

### Maze Generation

The maze is generated using a recursive backtracking algorithm. The `generate_maze` function creates a maze with the specified width and height, ensuring that the width and height are odd numbers. The `carve_passages_from` function recursively carves out passages in the maze.

### Maze Solving

The program includes two maze-solving algorithms:

1. **Depth-First Search (DFS)**: The `dfs` function implements the DFS algorithm to find a path from the start to the end of the maze.
2. **A\* Algorithm**: The `a_star` function implements the A\* algorithm to find the shortest path from the start to the end of the maze. The heuristic used is the Manhattan distance.

### Visualization

The `draw_maze` function uses Pygame to visualize the maze and the paths found by the DFS and A\* algorithms. The maze is displayed in a window, with the DFS path shown in red and the A\* path shown in blue.

## Example

To generate and solve a maze with a width and height of 75, you can use the following code:

```python
width, height = 75, 75
maze = generate_maze(width, height)
print_maze(maze)

start = (1, 0)
end = (width - 2, height - 1)
path_dfs = dfs(maze, start, end)
path_astar = a_star(maze, start, end)

if path_dfs:
    print("Path found by DFS:")
if path_astar:
    print("Path found by A*:")
draw_maze(maze, path_dfs, path_astar)
```
