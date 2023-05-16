import  random 
import math
m = [[0,0,1,0,0,0],
     [0,0,1,0,0,0],
     [1,1,0,1,1,0],
     [0,0,1,0,0,1],
     [0,0,1,0,0,1],
     [0,0,0,1,1,0]
]

def objetivo(estado):
    contador = len(estado)*[0]
    for x in estado:
        contador[x] = 1
    soma = 0
    for x in contador:
        soma += x
    return len(estado) - soma

def valido(estado):
    for i in range(len(m)):
        linha = m[i]
        for j in range(len(linha)):
            if(m[i][j]==1):
                if(estado[i] == estado[j]):
                    return False
    return True

def sucessor(estado):
    candidato = estado.copy()
    indice = random.randint(0,len(estado)-1)
    valor = random.randint(0,len(estado)-1)
    candidato[indice] = valor
    if(not valido(candidato)):
        return estado
    return candidato

def estado_inicial():
    inicial = []
    for i in range(len(m)):
        inicial.append(i)
    return inicial

def prob(delta_E,T):
    limite = math.exp(delta_E/T)
    sorteio = random.uniform(0,1)
    if(sorteio < limite):
        return True
    return False

atual = estado_inicial()
T = 1000

while(True):
        T = 0.999*T
        if(T < 0.00001):
            break
        proximo = sucessor(atual)
        delta_E = objetivo(proximo) - objetivo(atual)
        if(delta_E > 0 or prob(delta_E,T)):
           atual = proximo
print(atual)