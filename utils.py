def update_weights(G, congestion_data):
    for (u, v) in G.edges():
        base_weight = G[u][v]['base_weight']  # 원래 가중치
        congestion_factor = congestion_data.get(v, 1)  # 혼잡도 계수 (기본값 1)
        G[u][v]['weight'] = base_weight / congestion_factor  # 혼잡할수록 가중치 감소

def update_graph(G, congestion_data):
    update_weights(G, congestion_data)