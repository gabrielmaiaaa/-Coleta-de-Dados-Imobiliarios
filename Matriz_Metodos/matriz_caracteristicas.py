import numpy as np

def verificaAdjacencia(matriz, vi, vj):
    if matriz[vi][vj] > 0 or matriz[vj][vi] > 0:
        return True
    elif matriz[vi][vj] == 0 or matriz[vj][vi] == 0:
        return False


def tipoGrafo(instancia):
    matriz = np.array(instancia)
    linhas, colunas = instancia.shape
    tipo = 0 #colocando desde o começo o grafo como o tipo simples
    for i in range(0, linhas):
        for j in range(0, colunas):
            if matriz[i][j] != matriz[j][i]: #verifica se é um grafo dirigido
                tipo = 1
    for i in range(0, linhas):
        for j in range(0, colunas):
            if matriz[i][j] > 1: #verifica se o grafo tem arestas paralelas
                if tipo == 0: #caso seja simples
                    tipo = 20
                elif tipo == 1: #caso seja dirigido
                    tipo = 21
            elif matriz[i][i] > 0: #verifica se o grafo tem laços
                if tipo == 0 or tipo == 20: #caso seja simples ou seja multigrafo simples
                    tipo = 30
                elif tipo == 1 or tipo == 21: #caso seja dirigido ou um multigrafo dirigido
                    tipo = 31
    return tipo


def calcDensidade(matriz):
    #não importa o tipo, pois a formula vai ser a mesma
    matriz = np.array(matriz)
    linhas, colunas = matriz.shape
    arestas = np.sum(matriz)
    densidade = arestas/(linhas*(linhas-1))
    return round(densidade, 3)