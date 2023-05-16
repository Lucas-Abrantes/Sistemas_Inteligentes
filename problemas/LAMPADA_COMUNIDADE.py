import random

# Dados de entrada
houses = {'Casa 1': [1, 2, 3, 5], 'Casa 2': [2, 5], 'Casa 3': [1, 3, 4, 5], 'Casa 4': [4]}
lamps = {1: ['Casa 1', 'Casa 3'], 2: ['Casa 1', 'Casa 2'], 3: ['Casa 1', 'Casa 3'], 4: ['Casa 3', 'Casa 4'], 5: ['Casa 1', 'Casa 2', 'Casa 3']}

# Parâmetros do algoritmo genético
POP_SIZE = 5
GENERATIONS = 10
MUTATION_PROB = 0.1

# Função de fitness
def fitness(individual):
    # Verifica se todas as casas estão iluminadas
    for house in houses:
        if not any(lamp in individual for lamp in lamps if house in lamps[lamp]):
            return 99999
    # Retorna o número de lâmpadas usadas como fitness
    return len(individual)

# Gera um indivíduo aleatório
def generate_individual():
    return random.sample(sorted(lamps.keys()), random.randint(1, len(lamps)))

# Gera a população inicial
population = [generate_individual() for _ in range(POP_SIZE)]

# Executa o algoritmo genético
for generation in range(GENERATIONS):
    # Avalia a população atual
    scores = [fitness(individual) for individual in population]
    best_individual = population[scores.index(min(scores))]
    print(f'Geração {generation}: {best_individual} ({min(scores)})')
    # Gera a nova população
    new_population = []
    while len(new_population) < POP_SIZE:
        # Seleciona dois indivíduos aleatórios
        parent1 = random.choice(population)
        parent2 = random.choice(population)
        # Realiza o crossover
        child = parent1[:len(parent1)//2] + parent2[len(parent2)//2:]
        # Realiza a mutação
        if random.random() < MUTATION_PROB:
            gene_to_mutate = random.randint(0, len(child)-1)
            child[gene_to_mutate] = random.choice(list(lamps.keys()))
        # Adiciona o filho à nova população
        new_population.append(child)
    # Atualiza a população atual
    population = new_population

# Avalia a população final e exibe o melhor indivíduo
scores = [fitness(individual) for individual in population]
best_individual
