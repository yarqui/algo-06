# South Florida Inter-City Transportation Graph

## Overview

This project models a transportation network in South Florida using Python and NetworkX. Cities such as **Miami**, **Fort Lauderdale**, **Hollywood**, and others are represented as nodes. Roads connecting them are edges with distances in miles.

The graph is analyzed using graph algorithms including:

- **Breadth-First Search (BFS)**
- **Depth-First Search (DFS)**
- **Dijkstra’s Algorithm** for shortest path computation

---

## Algorithms Implemented

### ✅ DFS (Depth-First Search)

- Implemented manually using a stack
- Explores as far as possible along a branch before backtracking

### ✅ BFS (Breadth-First Search)

- Implemented manually using a queue
- Explores neighbors level by level

### ✅ Dijkstra's Algorithm (manual)

- Computes the shortest distance from each city to all others
- Uses a priority-selection approach over unvisited nodes
- Displays distances in miles

---

## Graph Properties Computed

- **Number of Nodes and Edges**
- **Degree Centrality**
- **Betweenness Centrality**

These help identify critical hubs and high-traffic routes in the network.

---

## Sample Output (Shortened for Display)

```
DFS path from Fort Lauderdale:
  Fort Lauderdale
  Dania Beach
  Hollywood
  Pembroke Pines
  Miramar
  Hialeah
  Miami

BFS path from Fort Lauderdale:
  Fort Lauderdale
  Dania Beach
  Hollywood
  Miramar
  Pembroke Pines
  Miami
  Hialeah

Dijkstra's shortest path lengths from each city:
From Miami:
  to Hialeah: 14 miles
  to Hollywood: 32 miles
  ...
```

---

## Dependencies

- Python 3.x
- `networkx`
- `matplotlib`

Install with:

```bash
pip install networkx matplotlib
```

---

## How to Run

Run:

```bash
python transport_graph.py
```

---

## Visualization

A spring layout visual of the transportation network is rendered using Matplotlib.

---

## Author

Coursework project demonstrating manual graph traversal and analysis in Python.
