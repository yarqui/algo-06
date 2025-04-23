# South Florida Inter-City Transportation Graph

## Overview

This project models a real-world inter-city transportation network in South Florida using the `networkx` Python library. Cities like **Miami**, **Hialeah**, **Hollywood**, **Dania Beach**, **Fort Lauderdale**, **Miramar**, and **Pembroke Pines** are represented as graph nodes. The roads between them are weighted edges indicating distances in miles.

We perform the following tasks:

- Graph construction and visualization
- Graph analysis using centrality metrics
- BFS and DFS traversals using `networkx.bfs_tree()` and `networkx.dfs_tree()`
- Comparison of BFS and DFS traversal paths from a common source

---

## Algorithms Used

### Breadth-First Search (BFS)

- Explores neighbors level-by-level
- Produces the shortest-path tree in terms of number of edges
- Implemented using `nx.bfs_tree()`

### Depth-First Search (DFS)

- Explores as deeply as possible before backtracking
- Produces a different tree structure compared to BFS
- Implemented using `nx.dfs_tree()`

---

## Example Output (From Source: Miami)

```
BFS path to Dania Beach: ['Miami', 'Hollywood', 'Dania Beach']
DFS path to Dania Beach: ['Miami', 'Miramar', 'Dania Beach']
```

As you can see:

- BFS prefers **level-wise exploration**, choosing Hollywood before going to Dania Beach.
- DFS goes **deep first**, reaching Miramar and then Dania Beach.

This highlights how traversal order depends on algorithm strategy.

---

## Analysis Metrics

- **Degree Centrality**: Reflects how many immediate connections a node has.
- **Betweenness Centrality**: Measures how often a node appears on shortest paths between other nodes.

These are printed for all nodes, allowing identification of key hubs (e.g., **Miramar**, **Hialeah**).

---

## Dependencies

- Python 3.x
- `networkx`
- `matplotlib`

Install them using:

```bash
pip install networkx matplotlib
```

---

## How to Run

Run:

```bash
python transport_graph.py
```

This will:

- Analyze the graph
- Print centrality metrics
- Show BFS and DFS paths from **Miami**
- Visualize the inter-city graph

---

## Author

Graph theory exploration project for coursework or educational demonstration.
