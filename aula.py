#python3 arquivo.py
#profundidade vai ser pilha, largura vai ser fila
grafo = [
    #0  1  2  3  4  5  6
    [0, 1, 1, 0, 1, 0, 0], #0
    [0, 0, 0, 0, 1, 1, 0], #1
    [0, 0, 0, 1, 1, 0, 0], #2
    [0, 0, 0, 0, 0, 0, 1], #3
    [0, 0, 0, 1, 0, 1, 1], #4
    [0, 0, 0, 1, 0, 0, 1], #5
    [0, 0, 0, 0, 0, 0, 0]  #6
]

pesos = [
    #0  1  2  3  4  5  6
    [0, 2, 1, 0, 3, 0, 0], #0
    [0, 0, 0, 0, 2, 3, 0], #1
    [0, 0, 0, 6, 9, 0, 0], #2
    [0, 0, 0, 0, 0, 0, 1], #3
    [0, 0, 0, 1, 0, 1, 3], #4
    [0, 0, 0, 2, 0, 0, 4], #5
    [0, 0, 0, 0, 0, 0, 0]  #6
]
origem = 0
destino = 6
solucao = []

def buscaProf(vertice, caminho, valor):

    if vertice == destino:
        aux = (caminho, valor)
        solucao.append(aux)
    else:
        for i in range(0, len(grafo[vertice])):
            if grafo[vertice][i] != 0:
                buscaProf(i, caminho+str(i)+" ", valor+pesos[vertice][i])

buscaProf(0, "0 ", 0)
for i in solucao:
    print(i)