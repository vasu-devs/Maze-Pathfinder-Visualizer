# 🎮 Maze Pathfinder Visualizer

An interactive **Pygame-based maze pathfinding visualizer** that demonstrates four classic pathfinding algorithms: **BFS**, **DFS**, **Dijkstra**, and **A***. Watch in real-time as different algorithms explore a randomly generated maze to find the shortest path from start to finish!

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Pygame](https://img.shields.io/badge/Pygame-2.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 📋 Table of Contents

- [Features](#-features)
- [Demo](#-demo)
- [Algorithms](#-algorithms)
- [Installation](#-installation)
- [Usage](#-usage)
- [Controls](#-controls)
- [Project Structure](#-project-structure)
- [Technical Details](#-technical-details)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

- **4 Pathfinding Algorithms**: Compare BFS, DFS, Dijkstra, and A* side-by-side
- **Real-time Visualization**: Watch algorithms explore the maze step-by-step
- **Procedural Maze Generation**: Randomly generated mazes using recursive backtracking
- **Interactive Controls**: Switch algorithms, regenerate mazes, and run searches on the fly
- **Performance Metrics**: Track path length and execution time for each algorithm
- **Color-Coded Display**: Each algorithm has unique colors for easy identification
- **Smooth Animation**: 60 FPS visualization for clear understanding of algorithm behavior

---

## 🎬 Demo

### Color Scheme

| Color | Meaning |
|-------|---------|
| 🟢 **Green** | Start point (top-left corner) |
| 🔴 **Red** | End point (bottom-right corner) |
| ⬜ **White** | Walkable paths |
| ⬛ **Black** | Walls/obstacles |
| 🔵 **Blue** | BFS explored cells |
| 🔴 **Red** | DFS explored cells |
| 🟢 **Green** | Dijkstra explored cells |
| 🟡 **Yellow** | A* explored cells |
| 🟠 **Orange** | Final shortest path |

---

## 🧠 Algorithms

### 1. **BFS (Breadth-First Search)**
- **Data Structure**: Queue (FIFO)
- **Strategy**: Explores all neighbors at current depth before moving deeper
- **Guarantee**: Finds shortest path in unweighted graphs
- **Time Complexity**: O(V + E)
- **Space Complexity**: O(V)
- **Best For**: Unweighted graphs, shortest path guarantee needed

### 2. **DFS (Depth-First Search)**
- **Data Structure**: Stack (LIFO)
- **Strategy**: Explores as far as possible along each branch before backtracking
- **Guarantee**: Does NOT guarantee shortest path
- **Time Complexity**: O(V + E)
- **Space Complexity**: O(V)
- **Best For**: Exploring all paths, memory-efficient depth exploration

### 3. **Dijkstra's Algorithm**
- **Data Structure**: Priority Queue (Min-Heap)
- **Strategy**: Always explores the least-cost node first
- **Guarantee**: Finds shortest path in weighted graphs
- **Time Complexity**: O((V + E) log V)
- **Space Complexity**: O(V)
- **Best For**: Weighted graphs with non-negative weights

### 4. **A\* (A-Star)**
- **Data Structure**: Priority Queue with Heuristic
- **Strategy**: Uses Manhattan distance heuristic to guide search toward goal
- **Guarantee**: Finds shortest path (with admissible heuristic)
- **Time Complexity**: O((V + E) log V)
- **Space Complexity**: O(V)
- **Best For**: Goal-directed search, optimal performance in many scenarios
- **Heuristic**: `h(n) = |x₁ - x₂| + |y₁ - y₂|` (Manhattan distance)

---

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/vasu-devs/Maze-Pathfinder-Visualizer.git
   cd Maze-Pathfinder-Visualizer
   ```

2. **Install dependencies**
   ```bash
   pip install pygame
   ```

3. **Run the visualizer**
   ```bash
   python yeah.py
   ```

---

## 🎮 Usage

1. **Launch the application** by running `python yeah.py`
2. **Select an algorithm** by pressing keys `1-4`
3. **Press SPACE** to run the selected algorithm
4. **Press R** to generate a new random maze
5. **Press ESC** to quit

### Example Workflow

```
1. Press '1' to select BFS
2. Press SPACE to watch BFS find the path
3. Press '4' to select A*
4. Press SPACE to compare A* performance
5. Press 'R' to generate a new maze and try again
```

---

## ⌨️ Controls

| Key | Action |
|-----|--------|
| **1** | Select BFS Algorithm |
| **2** | Select DFS Algorithm |
| **3** | Select Dijkstra Algorithm |
| **4** | Select A* Algorithm |
| **SPACE** | Run selected algorithm |
| **R** | Regenerate maze |
| **ESC** | Quit application |

---

## 📁 Project Structure

```
Maze-Pathfinder-Visualizer/
│
├── yeah.py              # Main application file
├── README.md            # Project documentation
└── __pycache__/         # Python cache files (auto-generated)
```

### Code Architecture

```python
# Configuration
- CELL_SIZE, MAZE_WIDTH, MAZE_HEIGHT, FPS
- Color definitions (WHITE, BLACK, BLUE, RED, etc.)

# Core Functions
- generate_maze()        # Recursive backtracking maze generation
- draw_maze()            # Renders maze to screen
- draw_ui()              # Displays controls and metrics

# Pathfinding Algorithms
- bfs()                  # Breadth-First Search
- dfs()                  # Depth-First Search
- dijkstra()             # Dijkstra's Algorithm
- a_star()               # A* Algorithm
- reconstruct_path()     # Builds final path from visited nodes

# Main Loop
- main()                 # Game loop and event handling
```

---

## 🔧 Technical Details

### Configuration Parameters

```python
CELL_SIZE = 15          # Pixel size of each maze cell
MAZE_WIDTH = 45         # Number of cells horizontally
MAZE_HEIGHT = 45        # Number of cells vertically
FPS = 60                # Animation frame rate
```

**Window Size**: 675x675 pixels (45 cells × 15 pixels)

### Maze Generation

- **Algorithm**: Recursive Backtracking (DFS-based)
- **Process**:
  1. Start with a grid full of walls
  2. Carve paths by randomly removing walls
  3. Use stack-based DFS to ensure perfect maze (one solution)
  4. Guarantees connectivity from start to end

### Path Reconstruction

The `reconstruct_path()` function traces backwards from the end point using parent pointers:

```python
visited = {cell: parent_cell}  # Each cell stores its parent
# Walk backward: end → parent → parent → ... → start
```

### Performance Metrics

- **Path Length**: Number of cells in the final path (excluding start)
- **Execution Time**: Wall-clock time from search start to completion (in seconds)

---

## 🤝 Contributing

Contributions are welcome! Here are some ideas for enhancements:

### Potential Improvements

- [ ] Add more algorithms (Greedy Best-First, Bidirectional Search)
- [ ] Implement weighted maze cells
- [ ] Add diagonal movement option
- [ ] Allow custom start/end points via mouse clicks
- [ ] Add step-by-step mode (pause/play controls)
- [ ] Save/load maze configurations
- [ ] Statistics comparison table for all algorithms
- [ ] Export visualization as GIF/video

### How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Pygame** - For providing an excellent 2D game development framework
- **Pathfinding Algorithms** - Classic computer science algorithms that power navigation systems worldwide
- Inspired by pathfinding visualizers and maze generation tutorials

---

## 📧 Contact

**Vasu** - [@vasu-devs](https://github.com/vasu-devs)

**Project Link**: [https://github.com/vasu-devs/Maze-Pathfinder-Visualizer](https://github.com/vasu-devs/Maze-Pathfinder-Visualizer)

---

## 📸 Screenshots

### Algorithm Comparison

**BFS (Blue)** - Explores uniformly in all directions
```
Pros: Guarantees shortest path, systematic exploration
Cons: Explores many unnecessary cells
```

**DFS (Red)** - Dives deep into one direction
```
Pros: Memory efficient, fast initial exploration
Cons: No shortest path guarantee, can take wrong paths
```

**Dijkstra (Green)** - Optimal for weighted graphs
```
Pros: Shortest path guarantee, handles weighted edges
Cons: Explores in all directions (slower than A*)
```

**A\* (Yellow)** - Guided by heuristic toward goal
```
Pros: Fastest to goal, optimal path, heuristic-guided
Cons: Requires good heuristic function
```

---

## ⚙️ Customization

### Adjust Maze Size

```python
MAZE_WIDTH = 60   # Make maze wider
MAZE_HEIGHT = 60  # Make maze taller
CELL_SIZE = 10    # Make cells smaller
```

### Change Animation Speed

```python
FPS = 120         # Faster visualization
FPS = 30          # Slower, easier to follow
```

### Modify Colors

```python
# Change algorithm colors in the color definitions section
BLUE = (100, 200, 255)    # Custom BFS color
ORANGE = (255, 128, 0)    # Custom path color
```

---

**Happy Pathfinding! 🗺️✨**
