import pygame
import random
import heapq
import time
from collections import deque


# --- Config ---
CELL_SIZE = 15      # Size of each maze cell in pixels (15x15 pixel squares)
MAZE_WIDTH = 45     # Number of cells horizontally in the maze grid
MAZE_HEIGHT = 45    # Number of cells vertically in the maze grid
FPS = 60            # Frames per second for visualization speed (controls animation smoothness)

# Colors
WHITE = (255, 255, 255)      # Maze paths (walkable cells)
BLACK = (0, 0, 0)            # Maze walls (obstacles)
BLUE = (50, 150, 255)        # BFS visited cells
RED = (255, 50, 50)          # DFS visited cells / End point
GREEN = (50, 255, 100)       # Dijkstra visited cells / Start point
YELLOW = (255, 255, 100)     # A* visited cells
ORANGE = (255, 165, 0)       # Final shortest path


ALGO_NAMES = ["BFS", "DFS", "Dijkstra", "A*"]

pygame.init()
pygame.font.init()
FONT = pygame.font.SysFont(None, 20)


screen = pygame.display.set_mode((MAZE_WIDTH * CELL_SIZE, MAZE_HEIGHT * CELL_SIZE))
pygame.display.set_caption("Maze Pathfinder Visualizer")
clock = pygame.time.Clock()

def generate_maze(width, height):
    maze = [[1 for _ in range(width)] for _ in range(height)]  # 1 = wall, 0 = path
    stack = [(0, 0)]
    maze[0][0] = 0

    while stack:
        x, y = stack[-1]
        neighbors = []
        for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == 1:
                neighbors.append((nx, ny))

        if neighbors:
            nx, ny = random.choice(neighbors)
            maze[ny][nx] = 0
            maze[y + (ny - y) // 2][x + (nx - x) // 2] = 0
            stack.append((nx, ny))
        else:
            stack.pop()

    return maze

# --- Drawing ---
def draw_maze(maze, visited=set(), path=set(), algo_color=BLUE, start=None, end=None):
    """Draw the maze grid to the screen.

    visited: iterable of visited (x,y) shown in algo_color
    path: set of (x,y) final path shown in Orange
    start/end: optional tuples to highlight start and end cells
    """
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            # base color: path or wall
            color = WHITE if maze[y][x] == 0 else BLACK
            # visited cells (during search)
            if (x, y) in visited:
                color = algo_color
            # final reconstructed path
            if (x, y) in path:
                color = ORANGE
            # start/end override
            if start is not None and (x, y) == start:
                color = GREEN
            if end is not None and (x, y) == end:
                color = RED

            pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# --- Pathfinding Algorithms ---

# BFS (Breadth-First Search)
# Data Structure: Queue (deque)
# Time Complexity: O(V + E) where V = vertices (cells), E = edges (connections)
# Space Complexity: O(V)
def bfs(maze, start, end):
    q = deque([start])
    visited = {start: None}
    while q:
        current = q.popleft()
        if current == end:
            break
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = current[0] + dx, current[1] + dy
            if 0 <= nx < len(maze[0]) and 0 <= ny < len(maze) and maze[ny][nx] == 0 and (nx, ny) not in visited:
                visited[(nx, ny)] = current
                q.append((nx, ny))
        draw_maze(maze, visited.keys(), algo_color=BLUE)
        pygame.display.flip()
        clock.tick(FPS)
    return reconstruct_path(visited, end)

# DFS (Depth-First Search)
# Data Structure: Stack (list)
# Time Complexity: O(V + E) where V = vertices (cells), E = edges (connections)
# Space Complexity: O(V)
def dfs(maze, start, end):
    stack = [start]
    visited = {start: None}
    while stack:
        current = stack.pop()
        if current == end:
            break
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = current[0] + dx, current[1] + dy
            if 0 <= nx < len(maze[0]) and 0 <= ny < len(maze) and maze[ny][nx] == 0 and (nx, ny) not in visited:
                visited[(nx, ny)] = current
                stack.append((nx, ny))
        draw_maze(maze, visited.keys(), algo_color=RED)
        pygame.display.flip()
        clock.tick(FPS)
    return reconstruct_path(visited, end)

# Dijkstra's Algorithm
# Data Structure: Priority Queue (min-heap)
# Time Complexity: O((V + E) log V) where V = vertices, E = edges
# Space Complexity: O(V)
def dijkstra(maze, start, end):
    pq = [(0, start)]
    visited = {start: None}
    dist = {start: 0}
    while pq:
        d, current = heapq.heappop(pq)
        if current == end:
            break
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = current[0] + dx, current[1] + dy
            if 0 <= nx < len(maze[0]) and 0 <= ny < len(maze) and maze[ny][nx] == 0:
                new_dist = d + 1
                if (nx, ny) not in dist or new_dist < dist[(nx, ny)]:
                    dist[(nx, ny)] = new_dist
                    visited[(nx, ny)] = current
                    heapq.heappush(pq, (new_dist, (nx, ny)))
        draw_maze(maze, visited.keys(), algo_color=GREEN)
        pygame.display.flip()
        clock.tick(FPS)
    return reconstruct_path(visited, end)

# A* (A-Star) Algorithm
# Data Structure: Priority Queue (min-heap) with heuristic (Manhattan distance)
# Time Complexity: O((V + E) log V) where V = vertices, E = edges
# Space Complexity: O(V)
def a_star(maze, start, end):
    pq = [(0, start)]
    visited = {start: None}
    g = {start: 0}
    while pq:
        _, current = heapq.heappop(pq)
        if current == end:
            break
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = current[0] + dx, current[1] + dy
            if 0 <= nx < len(maze[0]) and 0 <= ny < len(maze) and maze[ny][nx] == 0:
                temp_g = g[current] + 1
                if (nx, ny) not in g or temp_g < g[(nx, ny)]:
                    g[(nx, ny)] = temp_g
                    f = temp_g + abs(nx - end[0]) + abs(ny - end[1])
                    visited[(nx, ny)] = current
                    heapq.heappush(pq, (f, (nx, ny)))
        draw_maze(maze, visited.keys(), algo_color=YELLOW)
        pygame.display.flip()
        clock.tick(FPS)
    return reconstruct_path(visited, end)

# --- Path Reconstruction ---
def reconstruct_path(visited, end):
    path = set()
    node = end
    while node in visited and visited[node] is not None:
        path.add(node)
        node = visited[node]
    return path


def draw_ui(current_algo_idx, running_search, last_path_len=None, last_time=None):
    """Draw overlay UI: current selection, controls, and last result."""
    lines = [
        f"Algorithm: {ALGO_NAMES[current_algo_idx]}  (press 1-4 to change)",
        "Controls: [Space] run  [R] regenerate maze  [Esc] quit",
    ]
    if running_search:
        lines.append("Status: Searching...")
    else:
        lines.append("Status: Idle")
    if last_path_len is not None:
        lines.append(f"Last path length: {last_path_len}")
    if last_time is not None:
        lines.append(f"Time taken: {last_time:.4f} seconds")

    # draw each line with a small background for readability
    padding = 4
    x = 6
    y = 6
    # draw a contrasting background box for UI text so it is visible over white maze cells
    maxw = max(FONT.size(line)[0] for line in lines) + 12
    total_h = sum(FONT.size(line)[1] + 2 for line in lines) + 4
    ui_rect = pygame.Rect(4, 4, maxw, total_h)
    pygame.draw.rect(screen, (245, 245, 245), ui_rect)
    pygame.draw.rect(screen, (0,0,0), ui_rect, 1)
    for line in lines:
        surf = FONT.render(line, True, (0,0,0))
        rect = surf.get_rect(topleft=(x, y))
        screen.blit(surf, rect)
        y += rect.height + 2


# Dropdown removed — keyboard selection (1-4) is used instead

# --- Main Loop ---
def main():
    maze = generate_maze(MAZE_WIDTH, MAZE_HEIGHT)
    start = (0, 0)
    end = (MAZE_WIDTH - 1, MAZE_HEIGHT - 1)

    running = True
    algo_funcs = [bfs, dfs, dijkstra, a_star]

    algo_index = 0
    searching = False
    last_path_len = None
    last_time = None
    final_path = set()

    while running:
        screen.fill(BLACK)
        draw_maze(maze, path=final_path, start=start, end=end)
        draw_ui(algo_index, searching, last_path_len, last_time)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_1:
                    algo_index = 0
                    final_path = set()
                elif event.key == pygame.K_2:
                    algo_index = 1
                    final_path = set()
                elif event.key == pygame.K_3:
                    algo_index = 2
                    final_path = set()
                elif event.key == pygame.K_4:
                    algo_index = 3
                    final_path = set()
                elif event.key == pygame.K_r:
                    maze = generate_maze(MAZE_WIDTH, MAZE_HEIGHT)
                    last_path_len = None
                    last_time = None
                    final_path = set()
                elif event.key in (pygame.K_SPACE, pygame.K_RETURN):
                    searching = True
                    final_path = set()
                    
                    start_time = time.time()
                    path = algo_funcs[algo_index](maze, start, end)
                    end_time = time.time()
                    
                    final_path = path
                    draw_maze(maze, path=final_path, algo_color=ORANGE, start=start, end=end)
                    if path:
                        last_path_len = len(path)
                        last_time = end_time - start_time
                    else:
                        last_path_len = None
                        last_time = None
                    searching = False


    pygame.quit()

if __name__ == "__main__":
    main()
