import random

# Lista de itens com seu valor, peso e volume

itens = [(0.5278250968728682, 3.8223250028071334, 9.793806157959663), (0.5345615124227954, 3.447145401472379, 0.6468152148851247), (7.939795952467489, 4.092355196896432, 5.336237629812313), (4.87999696104728, 4.87437245102631, 6.422715815253146), (7.421255842609408, 9.369036702685223, 3.0007567888713393), (9.842285157721806, 5.407746144002427, 9.443121127515985), (9.730165519085599, 5.279563079544843, 0.38415938422414087), (3.205696243941171, 5.222093663097772, 5.715250979953179), (2.8030379035108277, 5.793174203171815, 1.122741743597242), (8.27626452697488, 2.561107477853107, 5.7887483288939965), (6.886628345999231, 2.450080314040153, 5.920306779300825), (4.192916339280606, 9.970857915129855, 5.271164202702553), (8.165140526387301, 5.402315594858978, 6.663476643896234), (1.780152737448204, 0.10432166249692565, 5.527553647653594), (0.5065955631174957, 6.195119115525767, 6.996862133184151), (5.23419784088932, 3.3133094985234033, 8.575624418484303), (0.9663844468158522, 5.354298648861051, 4.098620169275719), (2.3447517790443206, 0.9399381644540239, 6.390551757209495), (7.017793322301092, 9.727052913944101, 3.5856140555023863), (6.514398162927586, 9.487619612244272, 7.035383899019992), (7.471348857972483, 8.214152521047032, 4.982053382720071), (2.528444399325066, 0.018050097064232773, 6.036590987088305), (4.012589733203575, 5.246733095455984, 9.606796728554839), (1.214411237455596, 1.8733332713037132, 2.9322433635998513), (9.392057910289642, 0.6906707678020607, 7.502557855176284), (8.509490387647975, 6.481647057183848, 5.206750982488377), (4.338184227613736, 6.980179356481796, 2.928659342573247), (5.992405270085498, 9.772392622609487, 1.3737301227469234), (3.064188499576219, 6.475716440835933, 4.4705221641986785), (8.50803599613583, 3.0600582465594686, 3.9711956430286346), (7.687415004908054, 5.243448901028285, 3.6707527854209276), (8.492585703591345, 1.1398654659306073, 1.817483129208135), (8.818357488360542, 3.3523831244269306, 4.5376438709200055), (9.14435860411009, 1.155822730022379, 4.317267058250359), (0.7119771030371469, 3.9708479961873477, 0.6187012418533056), (0.9661477104364258, 8.225358591255764, 1.3493983036498014), (3.79656226509711, 6.387709467969497, 9.75949698626718), (0.5805472688214441, 0.2133750176734861, 8.128725325408118), (7.747046369023225, 8.513783572479005, 6.85159335144631), (3.41058053553518, 3.830255369285914, 9.855723490434617), (3.254640256553504, 2.768457231368097, 3.879939953700476), (1.5941274871735456, 0.7191529118878415, 2.6477670453714186), (2.2934660156703526, 4.674125437728243, 3.476131760425105), (8.897250584190711, 0.8626012151053908, 8.559956941043417), (2.7299695749744, 7.392170616958148, 7.419200671574588), (9.608891524167372, 1.506986295571121, 9.438499123159703), (7.12825344387973, 5.867886941844961, 2.2620973271838696), (4.577614440272705, 1.7928053403959077, 9.460882506403658), (9.762985792463168, 6.214672223724684, 7.598425581964133), (0.997411277081498, 5.54870160909565, 5.293585729242064)]

peso_Limite = 25
volume_Limite = 25

def objetivo(mochila):
    soma = 0
    for i in range(len(mochila)):
        if(mochila[i]):
            soma = soma+itens[i][0]
    return soma


def valido(mochila):
    peso_Total = 0
    for i in range(len(mochila)):
        if(mochila[i]):
            peso_Total = peso_Total+itens[i][1]
    if(peso_Total > peso_Limite):
        return False
    volume_Total = 0
    for i in range(len(mochila)):
        if(mochila[i]):
            volume_Total = volume_Total + itens[i][2]
    if(volume_Total > volume_Limite):
        return False
    
    return True

def modifica(mochila):
    aux = mochila.copy()
    i = random.randint(0, len(mochila) - 1)
    aux[i] = not aux[i]

    if(not valido(aux)):
        return mochila
    
    return aux

def estado_inicial():
    return len(itens)*[False]

def melhor_sucessor(mochila):
    atual = mochila
    for i in range(500):
        aux = modifica(atual)
        if(objetivo(aux) > objetivo(atual)):
            atual = aux
    return atual

melhor = estado_inicial()
for i in range(100):
    atual = estado_inicial()
    while(True):
        vizinho = melhor_sucessor(atual)
        if(objetivo(vizinho )<= objetivo(atual)):
            break
        atual = vizinho
        print(objetivo(atual))

    if(objetivo(atual) > objetivo(melhor)):
        melhor = atual
    print(objetivo(melhor))


print(atual)