import random

def generate_initial_population(G, nodes, population_size=10):
    population = []
    for _ in range(population_size):
        path = []
        current_node = random.choice(nodes[0])
        path.append(current_node)
        
        for i in range(1, len(nodes)):
            neighbors = list(G.successors(current_node))
            if neighbors:
                current_node = random.choice(neighbors)
                path.append(current_node)
            else:
                break
        population.append(path)
    return population
 
def fitness(G, path):
    prob = 1.0
    for i in range(len(path) - 1):
        if G.has_edge(path[i], path[i + 1]):
            prob *= G[path[i]][path[i + 1]]['weight']
        else:
            return 0  # 경로가 단절되면 확률 0
    return prob

def crossover(parent1, parent2):
    split = random.randint(1, min(len(parent1), len(parent2)) - 1)  # 랜덤 분할 지점 설정
    child = parent1[:split]
    for node in parent2[split:]:
        if node not in child:
            child.append(node)
    return child

def mutate(G, path, mutation_rate=0.3):  # 변이율 증가
    if random.random() < mutation_rate:
        index = random.randint(0, len(path) - 2)
        neighbors = list(G.successors(path[index]))
        if neighbors:
            path[index + 1] = random.choice(neighbors)
    return path

def genetic_algorithm(G, nodes, generations=50, population_size=10, top_n=3):
    population = generate_initial_population(G, nodes, population_size)
    
    for _ in range(generations):
        population = sorted(population, key=lambda p: fitness(G, p), reverse=True)
        new_population = population[:2]  # 상위 2개 개체 유지 (엘리트 선택)
        
        while len(new_population) < population_size:
            parent1, parent2 = random.choices(population[:7], k=2)  # 상위 7개 중 랜덤 선택
            child = crossover(parent1, parent2)
            child = mutate(G, child)
            new_population.append(child)
        
        population = new_population
    
    unique_paths = list({tuple(p): p for p in population}.values())  # 중복 제거
    top_paths = sorted(unique_paths, key=lambda p: fitness(G, p), reverse=True)[:top_n]
    return [(path, fitness(G, path)) for path in top_paths]