import numpy as np
import networkx as nx
from ga import genetic_algorithm
from utils import update_graph

def create_network(layer_sizes):
    np.random.seed(42)
    G = nx.DiGraph()
    nodes = []
    
    for i, size in enumerate(layer_sizes):
        nodes.append([f'L{i}_N{j}' for j in range(size)])
    
    for i in range(len(layer_sizes) - 1):
        for u in nodes[i]:
            for v in nodes[i + 1]:
                weight = np.random.rand()
                G.add_edge(u, v, weight=weight)
                G[u][v]['base_weight'] = weight
    
    return G, nodes, {edge: G[edge[0]][edge[1]]['base_weight'] for edge in G.edges()}


if __name__ == '__main__':
    layer_sizes = [10, 6, 6, 8]
    G, nodes, weights = create_network(layer_sizes)
    
    # 초기 혼잡도 설정 (1이면 정상, 2이면 2배 혼잡)
    congestion_data = {
        'L0_N3': 1.8,
        'L1_N1': 1.5,
        'L1_N2': 1.7,
        'L2_N0': 2.2,
        'L2_N3': 2.0
    }
    
    update_graph(G, congestion_data)
    
    best_paths = genetic_algorithm(G, nodes, top_n=3)
    
    for i, (path, prob) in enumerate(best_paths):
        print(f"Best Path {i+1}: {path}, Probability: {prob}")