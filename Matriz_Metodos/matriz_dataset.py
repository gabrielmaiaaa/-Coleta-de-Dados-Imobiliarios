# ''' importação da bilbioteca para realizar as funções '''
import numpy as np


# ''' função para armazenar os dados, contidos em um arquivo, em uma variavel '''
def criarMatriz(nome):
    instancia = np.loadtxt(f"Instancia/{nome}.txt", dtype=int)
    return instancia


# ''' função para criar novo arquivo '''
def salvarNumArquivo(instancia, nome):
    return np.savetxt(f"Instancia/{nome}.txt", instancia, fmt="%d")
