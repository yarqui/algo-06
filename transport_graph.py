from collections import deque
import networkx as nx
import matplotlib.pyplot as plt


def create_graph(edges):
    G = nx.Graph()
    G.add_weighted_edges_from(edges)
    return G


def analyze_graph(graph):
    num_nodes = graph.number_of_nodes()
    num_edges = graph.number_of_edges()
    degree_centrality = nx.degree_centrality(graph)
    betweenness_centrality = nx.betweenness_centrality(graph)

    print("Number of edges:", num_edges)
    print("Number of vertices:", num_nodes)
    print("\nCentrality degree:", degree_centrality)
    print("Betweenness centrality:", betweenness_centrality)

    # BFS & DFS
    source = "Fort Lauderdale"
    dfs_path(graph, source)
    bfs_path(graph, source)

    # Dijkstra
    print("\nDijkstra's shortest path lengths from each city:")
    for source in graph.nodes:
        lengths = dijkstra(graph, source)
        print(f"\nFrom {source}:")
        for target, distance in lengths.items():
            print(f"  to {target}: {distance} miles")


def dfs_path(graph, start_vertex):
    visited = set()
    stack = [start_vertex]
    print(f"\nDFS path from {start_vertex}: ")

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            print(f"  {vertex}")
            visited.add(vertex)
            neighbors = list(graph[vertex])
            stack.extend(reversed(neighbors))


def bfs_path(graph, start_vertex):
    visited = set()
    queue = deque([start_vertex])
    print(f"\nBFS path from {start_vertex}: ")

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(f"  {vertex}")
            visited.add(vertex)
            queue.extend([n for n in graph[vertex] if n not in visited])


def dijkstra(graph, start):
    distances = {vertex: float("infinity") for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.nodes)

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float("infinity"):
            break

        for neighbor, attrs in graph[current_vertex].items():
            weight = attrs["weight"]
            distance = distances[current_vertex] + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance

        unvisited.remove(current_vertex)

    return distances


def draw_graph(graph):
    pos = nx.spring_layout(graph, seed=42)
    nx.draw_networkx(graph, pos=pos, node_size=1500)
    plt.title("South Florida inter-city connection")
    plt.show()


def main():
    edges = [
        ("Miami", "Hialeah", 14),
        ("Miami", "Hollywood", 32),
        ("Miami", "Miramar", 35),
        ("Hialeah", "Miramar", 25),
        ("Hollywood", "Dania Beach", 5),
        ("Dania Beach", "Fort Lauderdale", 7),
        ("Dania Beach", "Miramar", 18),
        ("Miramar", "Pembroke Pines", 6),
        ("Pembroke Pines", "Hollywood", 12),
        ("Hialeah", "Pembroke Pines", 22),
    ]

    G = create_graph(edges=edges)
    analyze_graph(G)
    draw_graph(G)


if __name__ == "__main__":
    main()
