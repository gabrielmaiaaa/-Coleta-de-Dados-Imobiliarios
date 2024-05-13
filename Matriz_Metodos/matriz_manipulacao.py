import numpy as np

def insereAresta(matriz, vi, vj):
    matriz = np.array(matriz)
    matriz[vi][vj] = matriz[vi][vj] + 1
    matriz[vj][vi] = matriz[vj][vi] + 1
    return matriz


def insereVertice(matriz, vi):
    matriz = np.array(matriz)
    linhas, colunas = matriz.shape
    matriznova = np.zeros((vi, vi), dtype=int)
    matriznova = np.array(matriznova)
    for i in range(0, linhas):
        for j in range(0, colunas):
            matriznova[i][j] = matriz[i][j]
    return matriznova


def removeAresta(matriz, vi, vj):
    matriz = np.array(matriz)
    matriz[vi][vj] = matriz[vi][vj] - 1
    matriz[vj][vi] = matriz[vj][vi] - 1
    return matriz


def removeVertice(matriz, vi):
    matriz = np.array(matriz)
    linhas, colunas = matriz.shape
    for i in range(0, linhas):
        matriz[vi][i] = -1
        matriz[i][vi] = -1
    return matriz