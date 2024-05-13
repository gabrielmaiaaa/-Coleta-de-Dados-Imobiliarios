
def insereArestaLista(listaAdj, vi, vj):
    listaAdj[vi].append(vj)
    listaAdj[vj].append(vi)
    for coluna, elementos in listaAdj.items():
        elementos.sort()
    return listaAdj


def removeArestaLista(listaAdj, vi, vj):
    if vi in listaAdj[vj]:
        listaAdj[vj].remove(vi)
    if vj in listaAdj[vi]:
        listaAdj[vi].remove(vj)
    return listaAdj


def insereVerticeLista(listaAdj):
    tamanho = len(listaAdj)
    listaAdj[tamanho] = []
    return listaAdj

def removeVerticeLista(listaAdj, vi):
    listaAdj.pop(vi)
    tamanho = len(listaAdj)
    for qtd in range(0, tamanho):
        for coluna, valor in listaAdj.items():
            if vi in valor:
                valor.remove(vi)
    return listaAdj