import random
import math

def distancia(p1, p2):
    """Calcula a distância euclidiana entre dois pontos."""
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def cobertura(posicoes_antenas, posicoes_moradores, alcance):
    """Calcula o número de moradores cobertos por cada antena."""
    cobertura = [0] * len(posicoes_antenas)
    for i, a in enumerate(posicoes_antenas):
        for m in posicoes_moradores:
            if distancia(a, m) <= alcance:
                cobertura[i] += 1
    return cobertura

def simulated_annealing(posicoes_moradores, num_antenas, alcance, temperatura_inicial=1000, taxa_resfriamento=0.99):
    """Executa o algoritmo de simulated annealing para encontrar a posição das antenas que cobrem o máximo de moradores."""
    # Gera uma solução inicial aleatória
    posicoes_antenas = [random.choice(posicoes_moradores) for _ in range(num_antenas)]
    melhor_estado = posicoes_antenas[:]
    melhor_cobertura = cobertura(melhor_estado, posicoes_moradores, alcance)
    
    # Executa o algoritmo até a temperatura atingir o limite
    temperatura = temperatura_inicial
    while temperatura > 1:
        # Gera um novo estado a partir do estado atual
        novo_estado = posicoes_antenas[:]
        i = random.randint(0, num_antenas-1)
        novo_estado[i] = (random.uniform(0, 100), random.uniform(0, 100))
        
        # Avalia o novo estado
        nova_cobertura = cobertura(novo_estado, posicoes_moradores, alcance)
        
        # Aceita ou rejeita o novo estado com base na função de custo e na temperatura atual
        delta_custo = sum(nova_cobertura) - sum(melhor_cobertura)
        if delta_custo > 0 or random.random() < math.exp(delta_custo / temperatura):
            posicoes_antenas = novo_estado[:]
            melhor_cobertura = nova_cobertura[:]
        
        # Atualiza o melhor estado encontrado até agora
        if sum(melhor_cobertura) > sum(cobertura(melhor_estado, posicoes_moradores, alcance)):
            melhor_estado = posicoes_antenas[:]
        
        # Resfria a temperatura
        temperatura *= taxa_resfriamento
    
    return melhor_estado

# Exemplo de uso
posicoes_moradores = [(0, 0), (0, 50), (50, 0), (50, 50), (25, 25), (75, 75)]
num_antenas = 3
alcance = 5

melhor_estado = simulated_annealing(posicoes_moradores, num_antenas, alcance, temperatura_inicial=1000, taxa_resfriamento=0.99)

print("Posições das antenas:")
for antena in melhor_estado:
    print(antena)
