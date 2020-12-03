from dijkstar import Graph, find_path
import matplotlib.pyplot as plt
import networkx as nx
def d():
    graph = Graph()
    graph.add_edge(1, 2, 0)
    graph.add_edge(2, 3, -2)
    graph.add_edge(1, 3, -1)
    graph.add_edge(3, 4, 1)
    print(find_path(graph, 1, 4))
    #elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] > 1]
    #esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] <= 1]

    
    # pos = nx.spring_layout(G)  # positions for all nodes

    # # nodes
    # nx.draw_networkx_nodes(G, pos, node_size=700)

    # # edges
    # nx.draw_networkx_edges(G, pos, edgelist=elarge, width=6)
    # nx.draw_networkx_edges(
    #     G, pos, edgelist=esmall, width=6, alpha=0.5, edge_color="b", style="dashed"
    # )

    # # labels
    # nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")

    # plt.axis("off")
    # plt.show()
#d()
#print(s)
from dijkstar import Graph, find_path
def g():
    graph = nx.DiGraph()
    graph.add_edge(1, 2, weight = 0)
    #graph.add_edge(2, 3, weight = -2)
    graph.add_edge(1, 3, weight = -1)
    graph.add_edge(3, 4, weight = 1)
    #print(nx.dijkstra_path(graph, 1, 4))
    print(nx.bellman_ford_path(graph, 1, 4))
g()