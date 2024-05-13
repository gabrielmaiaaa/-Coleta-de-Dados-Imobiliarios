def criaListaAdjacencias(matriz):
    dicionario = {}
    for chave in range(len(matriz)):
        dicionario[chave] = []
        for j in range(len(matriz)):
            if matriz[chave][j] > 0:
                dicionario[chave].append(j)
    return dicionario


def listaAdjacneteInversa(matrizAdj):
    dicionario = {}
    for chave in range(len(matrizAdj)):
        dicionario[chave] = []
        for j in range(len(matrizAdj) - 1, -1, -1):
            if matrizAdj[chave][j] > 0:
                dicionario[chave].append(j)
    return dicionario


def verificaAdjacenciaLista(listaAdj, vi, vj):
    if vi in listaAdj[vj]:
        return True
    else:
        return False


def tipoGrafoLista(listaAdj):
    tipo = 0  # colocando desde o começo o grafo como o tipo simples
    tamanho = len(listaAdj)
    maisDeUm = []
    for chave in range(0, tamanho):
        for indice, valor in enumerate(listaAdj[chave]):
            if valor not in listaAdj[chave] or chave not in listaAdj[valor]:  # verifica se é um grafo dirigido
                tipo = 1
    for chave in range(0, tamanho):
        for indice, valor in enumerate(listaAdj[chave]):
            if (chave, valor) in maisDeUm:  # verifica se o grafo tem arestas paralelas
                if tipo == 0:  # caso seja simples
                    tipo = 20
                elif tipo == 1:  # caso seja dirigido
                    tipo = 21
            if valor == chave:  # verifica se o grafo tem laços
                if tipo == 0 or tipo == 20:  # caso seja simples ou seja multigrafo simples
                    tipo = 30
                elif tipo == 1 or tipo == 21:  # caso seja dirigido ou um multigrafo dirigido
                    tipo = 31
            maisDeUm.append((chave, valor))
    return tipo


def calcDensidadeLista(listaAdj):
    arestas = 0
    linhas = len(listaAdj)
    for indice, valor in listaAdj.items():
        arestas += len(valor)
    densidade = arestas / (linhas * (linhas - 1))
    return round(densidade, 3)
