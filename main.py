import random
import pygame
import sys
import time
import heapq

def print_maze(maze):
    for row in maze:
        print(''.join(row))

def carve_passages_from(maze, x, y, width, height):
    maze[y][x] = ' '
    directions = [(0, -2), (0, 2), (-2, 0), (2, 0)]
    random.shuffle(directions)

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 < nx < width and 0 < ny < height and maze[ny][nx] == '#':
            maze[y + dy//2][x + dx//2] = ' '
            carve_passages_from(maze, nx, ny, width, height)

def generate_maze(width, height):
    if width % 2 == 0 or height % 2 == 0:
        raise ValueError("Width and height must be odd.")

    maze = [['#'] * width for _ in range(height)]
    start_x, start_y = random.randrange(1, width, 2), random.randrange(1, height, 2)
    carve_passages_from(maze, start_x, start_y, width, height)

    # Ensure the entrance and exit are open
    maze[0][1] = ' '
    maze[height-1][width-2] = ' '

    return maze

def dfs(maze, start, end):
    stack = [start]
    visited = set()
    visited.add(start)
    path = []

    while stack:
        x, y = stack.pop()
        path.append((x, y))

        if (x, y) == end:
            return path

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(maze[0]) and 0 <= ny < len(maze) and maze[ny][nx] == ' ' and (nx, ny) not in visited:
                stack.append((nx, ny))
                visited.add((nx, ny))

    return None

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(maze, start, end):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}

    while open_set:
        current = heapq.heappop(open_set)[1]

        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < len(maze[0]) and 0 <= neighbor[1] < len(maze) and maze[neighbor[1]][neighbor[0]] == ' ':
                tentative_g_score = g_score[current] + 1

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, end)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None

def draw_maze(maze, path_dfs=None, path_astar=None):
    pygame.init()
    cell_size = 20
    width, height = len(maze[0]), len(maze)
    screen = pygame.display.set_mode((width * cell_size, height * cell_size))
    pygame.display.set_caption("Maze Solver")

    screen.fill((255, 255, 255))

    for y in range(height):
        for x in range(width):
            if maze[y][x] == '#':
                pygame.draw.rect(screen, (0, 0, 0), (x * cell_size, y * cell_size, cell_size, cell_size))

    pygame.display.flip()
    time.sleep(3)  # Pause to show the maze before drawing the paths

    if path_dfs:
        for x, y in path_dfs:
            pygame.draw.rect(screen, (255, 0, 0), (x * cell_size, y * cell_size, cell_size, cell_size))
            pygame.display.flip()
            time.sleep(0.001)  # Delay to show the DFS path being drawn

    if path_astar:
        for x, y in path_astar:
            pygame.draw.rect(screen, (0, 0, 255), (x * cell_size, y * cell_size, cell_size, cell_size))
            pygame.display.flip()
            time.sleep(0.01)  # Delay to show the A* path being drawn

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

# Exemple d'utilisation
width, height = 75, 75  # Change la taille du labyrinthe ici
maze = generate_maze(width, height)
print_maze(maze)

start = (1, 0)
end = (width - 2, height - 1)
path_dfs = dfs(maze, start, end)
path_astar = a_star(maze, start, end)

if path_dfs:
    print("Chemin trouvé par DFS :")
if path_astar:
    print("Chemin trouvé par A* :")
draw_maze(maze, path_dfs, path_astar)
