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
    print("Centrality degree:", degree_centrality)
    print("Betweenness centrality:", betweenness_centrality)


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
