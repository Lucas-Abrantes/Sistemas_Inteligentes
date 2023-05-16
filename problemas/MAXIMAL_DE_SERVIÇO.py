import numpy as np

def avaliar_solucao(solucao, matriz_distritos, tempo_maximo):
    tempo_total = 0
    for i in range(len(matriz_distritos)):
        tempo_minimo = np.inf
        for j in range(len(solucao)):
            if solucao[j] == 1:
                tempo_minimo = min(tempo_minimo, matriz_distritos[i][j])
        tempo_total += tempo_minimo
    return tempo_total / tempo_maximo

def gerar_solucao_inicial(num_distritos):
    solucao = np.zeros(num_distritos)
    num_centros = np.random.randint(1, num_distritos + 1)
    indices = np.random.choice(num_distritos, num_centros, replace=False)
    for i in indices:
        solucao[i] = 1
    return solucao

def gerar_vizinho(solucao):
    vizinho = solucao.copy()
    if np.sum(solucao) == 1:
        indices = np.where(solucao == 0)[0]
    else:
        indices = np.where(solucao == 1)[0]
    i = np.random.choice(indices)
    vizinho[i] = 1 - vizinho[i]
    return vizinho

def temperatura(t, t0, alpha):
    return t0 * alpha ** t

def tempera_simulada(matriz_distritos, tempo_maximo, t0=100, alpha=0.99, num_iteracoes=10000):
    solucao_atual = gerar_solucao_inicial(len(matriz_distritos))
    avaliacao_atual = avaliar_solucao(solucao_atual, matriz_distritos, tempo_maximo)
    melhor_solucao = solucao_atual
    melhor_avaliacao = avaliacao_atual
    for t in range(num_iteracoes):
        vizinho = gerar_vizinho(solucao_atual)
        avaliacao_vizinho = avaliar_solucao(vizinho, matriz_distritos, tempo_maximo)
        delta = avaliacao_vizinho - avaliacao_atual
        if delta < 0:
            solucao_atual = vizinho
            avaliacao_atual = avaliacao_vizinho
            if avaliacao_vizinho < melhor_avaliacao:
                melhor_solucao = vizinho
                melhor_avaliacao = avaliacao_vizinho
        else:
            prob = np.exp(-delta / temperatura(t, t0, alpha))
            if np.random.rand() < prob:
                solucao_atual = vizinho
                avaliacao_atual = avaliacao_vizinho
    indices = np.where(melhor_solucao == 1)[0]
    return indices.tolist()
matriz_distritos = [[0, 2, 4, 6], [2, 0, 3, 5], [4, 3, 0, 4], [6, 5, 4, 0]]
tempo_maximo = 20
distritos_escolhidos = tempera_simulada(matriz_distritos, tempo_maximo)
print(distritos_escolhidos)
