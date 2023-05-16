import random
import math

def calc_potencia(lampadas, solucao):
    # Calcula a potência total das lâmpadas da solução
    potencia_total = 0
    for lampada in solucao:
        potencia_total += lampadas[lampada]
    return potencia_total

def temperatura_inicial(potencia_atual, lampadas):
    # Define a temperatura inicial do algoritmo
    temperatura_inicial = 2 * potencia_atual
    return temperatura_inicial

def vizinho_aleatorio(solucao_atual, casas):
    # Gera um vizinho aleatório a partir da solução atual
    nova_solucao = list(solucao_atual)
    casa = random.randint(0, len(casas)-1)
    lampadas_casa = casas[casa]
    lampada = random.randint(0, len(lampadas_casa)-1)
    nova_solucao[casa] = lampadas_casa[lampada]
    return nova_solucao

def probabilidade(energia_atual, energia_vizinha, temperatura):
    # Calcula a probabilidade de aceitação da solução vizinha
    if energia_vizinha < energia_atual:
        return 1.0
    else:
        return math.exp((energia_atual - energia_vizinha) / temperatura)

def tempera_simulada(lampadas, casas, max_iteracoes=10000):
    # Executa o algoritmo de tempera simulada
    solucao_atual = [random.choice(casas[i]) for i in range(len(casas))]
    potencia_atual = calc_potencia(lampadas, solucao_atual)
    temperatura = temperatura_inicial(potencia_atual, lampadas)
    melhor_solucao = list(solucao_atual)
    melhor_potencia = potencia_atual
    
    for i in range(max_iteracoes):
        vizinho = vizinho_aleatorio(solucao_atual, casas)
        potencia_vizinha = calc_potencia(lampadas, vizinho)
        prob = probabilidade(potencia_atual, potencia_vizinha, temperatura)
        if prob > random.random():
            solucao_atual = list(vizinho)
            potencia_atual = potencia_vizinha
        if potencia_atual < melhor_potencia:
            melhor_solucao = list(solucao_atual)
            melhor_potencia = potencia_atual
        temperatura = temperatura * 0.99 # taxa de resfriamento
    
    return melhor_solucao


lampadas = [40, 60, 100, 20, 50]
casas = [[0, 2], [0, 3], [1, 3], [1, 4], [2, 4]]

conjunto_ligado = tempera_simulada(lampadas, casas)

print("Lâmpadas a serem ligadas:", conjunto_ligado)



import random
import math

O comando "import" é usado para importar módulos (bibliotecas) Python que contêm funções e objetos específicos que podem ser úteis no programa. O módulo "random" contém funções para gerar números aleatórios e o módulo "math" contém funções matemáticas úteis.

def calc_potencia(lampadas, solucao):

Esta é uma função que recebe como entrada duas listas: "lampadas" e "solucao". A lista "lampadas" contém a potência de cada lâmpada e a lista "solucao" contém as lâmpadas que devem ser ligadas para iluminar todas as casas. A função calcula a potência total das lâmpadas na solução, somando as potências das lâmpadas da lista "lampadas" cujos índices estão presentes na lista "solucao". O resultado é retornado como saída da função.

def temperatura_inicial(potencia_atual, lampadas):

Esta é uma função que recebe como entrada dois valores: "potencia_atual" e "lampadas". O valor "potencia_atual" é a potência total das lâmpadas na solução atual e "lampadas" é a lista de potências de lâmpadas. A função define a temperatura inicial do algoritmo multiplicando a potência atual por 2 e retornando o resultado como saída da função.

def vizinho_aleatorio(solucao_atual, casas):

Esta é uma função que recebe como entrada duas listas: "solucao_atual" e "casas". A lista "solucao_atual" contém as lâmpadas que devem ser ligadas na solução atual e "casas" contém a lista de lâmpadas associadas a cada casa. A função gera um vizinho aleatório a partir da solução atual, escolhendo aleatoriamente uma casa e uma lâmpada associada a essa casa. Em seguida, atualiza a lista "solucao_atual" com a lâmpada escolhida. A nova solução é retornada como saída da função.

def probabilidade(energia_atual, energia_vizinha, temperatura):

Esta é uma função que recebe como entrada três valores: "energia_atual", "energia_vizinha" e "temperatura". Os valores de "energia_atual" e "energia_vizinha" são a potência total das lâmpadas nas soluções atual e vizinha, respectivamente, e "temperatura" é a temperatura atual do algoritmo. A função calcula a probabilidade de aceitação da solução vizinha, usando a equação de Boltzmann. Se a energia da solução vizinha for menor que a energia da solução atual, a função retorna 1 (aceita a solução vizinha). Caso contrário, calcula a probabilidade de aceitação da solução vizinha e a retorna como saída da função.

def tempera_simulada(lampadas, casas, max_iteracoes=10000):

Esta é a função principal que executa o algoritmo de simulação de têmpera. Recebe como entrada a lista "lampadas" com as potências de cada lâmpada, a lista "casas





User
Continue a explicação
ChatGPT
O próximo passo do código é inicializar algumas variáveis, incluindo a solução inicial, a potência atual da solução inicial e a temperatura inicial do algoritmo. Para a solução inicial, é gerada uma lista de soluções aleatórias para cada casa, escolhendo uma lâmpada aleatória que está associada a cada casa. A potência total da solução inicial é então calculada usando a função "calc_potencia" definida anteriormente. A temperatura inicial é calculada como duas vezes a potência atual.

Em seguida, o algoritmo executa o loop principal com um número máximo de iterações (definido como 10000, por padrão). Em cada iteração, é gerado um vizinho aleatório da solução atual usando a função "vizinho_aleatorio". Essa função escolhe aleatoriamente uma casa e uma lâmpada associada a essa casa e troca a lâmpada selecionada pela lâmpada atualmente associada à casa.

A potência total da solução vizinha é calculada usando a função "calc_potencia". Em seguida, a probabilidade de aceitar a solução vizinha é calculada usando a função "probabilidade". Se a probabilidade de aceitação for maior que um número aleatório entre 0 e 1, a solução atual é atualizada para a solução vizinha. Caso contrário, a solução atual permanece a mesma.

Em seguida, é verificado se a potência da solução atual é menor do que a potência da melhor solução encontrada até agora. Se for o caso, a melhor solução é atualizada para a solução atual. Finalmente, a temperatura é atualizada multiplicando-se por um fator de resfriamento (definido como 0,99 por padrão) a cada iteração.

Após a execução do loop principal, a função retorna a melhor solução encontrada pelo algoritmo de tempera simulada, que é a lista de lâmpadas a serem ligadas para garantir a iluminação de todas as casas da comunidade. O resultado é então impresso na tela usando a função "print".