import numpy as np
import networkx as nx
from ga import genetic_algorithm

def create_network(layer_sizes):
    np.random.seed(42)
    G = nx.DiGraph()
    
    nodes = []
    for i, size in enumerate(layer_sizes):
        nodes.append([f'L{i}_N{j}' for j in range(size)])
    
    weights = {}
    for i in range(len(layer_sizes) - 1):
        for u in nodes[i]:
            for v in nodes[i + 1]:
                weight = np.random.rand()
                G.add_edge(u, v, weight=weight)
                weights[(u, v)] = weight
    
    return G, nodes, weights


if __name__ == '__main__':
    layer_sizes = [8, 5, 4]
    G, nodes, weights = create_network(layer_sizes)
    best_path, best_prob = genetic_algorithm(G, nodes)
    
    print("Best Path:", best_path)
    print("Best Probability:", best_prob)