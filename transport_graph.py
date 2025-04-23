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

    # BFS & DFS
    source = "Miami"
    bfs_tree = nx.bfs_tree(graph, source)
    dfs_tree = nx.dfs_tree(graph, source)

    print("Number of edges:", num_edges)
    print("Number of vertices:", num_nodes)
    print("\nCentrality degree:", degree_centrality)
    print("Betweenness centrality:", betweenness_centrality)

    print("\nSearching paths from Miami using NetworkX methods:")
    for target in bfs_tree.nodes:
        print(f"BFS path to {target}:", nx.shortest_path(bfs_tree, source, target))

    for target in dfs_tree.nodes:
        print(f"DFS path to {target}:", nx.shortest_path(dfs_tree, source, target))

    # Dijkstra
    print("\nDijkstra's shortest path lengths from each city:")
    for source in graph.nodes:
        lengths = nx.single_source_dijkstra_path_length(graph, source)
        print(f"\nFrom {source}:")
        for target, distance in lengths.items():
            print(f"  to {target}: {distance} miles")


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
