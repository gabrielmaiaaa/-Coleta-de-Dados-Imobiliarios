import time
import numpy as np


def ColetaDeDados(matriz, lista, v, visitados=None, V=None):
    if visitados is None:
        visitados = []
        V = [v]
    for adj in lista[v]:
        if f"{v}, {adj}" not in visitados and f"{adj}, {v}" not in visitados:
            if adj != V[0]:
                if ruaSemSaida(lista, v, visitados) == v:
                    visitados.append(f"{v}, {adj}")
                    ColetaDeDados(matriz, lista, adj, visitados, V)
                    visitados.append(f"{adj}, {v}")
                else:
                    i = ruaSemSaida(lista, v, visitados)
                    if f"{v}, {i}" not in visitados and f"{i}, {v}" not in visitados:
                        visitados.append(f"{v}, {i}")
                        visitados.append(f"{i}, {v}")
                        if f"{v}, {adj}" not in visitados and f"{adj}, {v}" not in visitados:
                            visitados.append(f"{v}, {adj}")
                            ColetaDeDados(matriz, lista, adj, visitados, V)
                            visitados.append(f"{adj}, {v}")
            else:
                visitados.append(f"{v}, {adj}")
                print(visitados)


def ColetaDados1(matriz, v, lista, visitados, conhecidos=None, V=None):
    if conhecidos is None:
        conhecidos = []
        V = [v]
    for adj in lista[v]:
        if f"{v}, {adj}" not in visitados and f"{adj}, {v}" not in visitados:
            if adj != V[0]:
                if ruaSemSaida(lista, v, visitados) == v:
                    casas = matriz[v][adj]
                    matriz[v][adj] -= casas
                    matriz[adj][v] -= casas
                    visitados.append(f"{v}, {adj}")
                    conhecidos.append(f"{v}, {adj}")
                    time.sleep(casas / 100)
                    ColetaDados1(matriz, adj, lista, visitados, conhecidos, V)
                    visitados.append(f"{adj}, {v}")
                    conhecidos.append(f"{adj}, {v}")
                else:
                    i = ruaSemSaida(lista, v, visitados)
                    if f"{v}, {i}" not in visitados and f"{i}, {v}" not in visitados:
                        casas = matriz[v][i]
                        matriz[v][i] -= casas
                        matriz[i][v] -= casas
                        visitados.append(f"{v}, {i}")
                        visitados.append(f"{i}, {v}")
                        conhecidos.append(f"{v}, {i}")
                        conhecidos.append(f"{i}, {v}")
                        time.sleep(casas / 100)
                        if f"{v}, {adj}" not in visitados and f"{adj}, {v}" not in visitados:
                            casas = matriz[v][adj]
                            matriz[v][adj] -= casas
                            matriz[adj][v] -= casas
                            visitados.append(f"{v}, {adj}")
                            conhecidos.append(f"{v}, {adj}")
                            time.sleep(casas / 100)
                            ColetaDados1(matriz, adj, lista, visitados, conhecidos, V)
                            visitados.append(f"{adj}, {v}")
                            conhecidos.append(f"{adj}, {v}")
            elif adj == V[0] and verificaOutros(lista, v, visitados):
                j = valor(lista, v, visitados)
                casas = matriz[v][j]
                matriz[v][j] -= casas
                matriz[j][v] -= casas
                visitados.append(f"{v}, {j}")
                time.sleep(casas / 100)
                ColetaDados1(matriz, j, lista, visitados, conhecidos, V)
                visitados.append(f"{j}, {v}")
                conhecidos.append(f"{j}, {v}")
                if f"{v}, {adj}" not in visitados and f"{adj}, {v}" not in visitados:
                    casas = matriz[v][adj]
                    matriz[v][adj] -= casas
                    matriz[adj][v] -= casas
                    visitados.append(f"{v}, {adj}")
                    conhecidos.append(f"{v}, {adj}")
    if v == V[0]:
        print(conhecidos)


def ColetaDados2(matriz, v, lista, visitados, conhecidos=None, V=None):
    if conhecidos is None:
        conhecidos = []
        V = [v]
    for adj in lista[v]:
        if f"{v}, {adj}" not in visitados and f"{adj}, {v}" not in visitados:
            if adj != V[0]:
                if ruaSemSaidaOP(lista, v, visitados) == v:
                    casas = matriz[v][adj]
                    matriz[v][adj] -= casas
                    matriz[adj][v] -= casas
                    visitados.append(f"{v}, {adj}")
                    conhecidos.append(f"{v}, {adj}")
                    time.sleep(casas / 100)
                    ColetaDados2(matriz, adj, lista, visitados, conhecidos, V)
                    visitados.append(f"{adj}, {v}")
                    conhecidos.append(f"{adj}, {v}")
                else:
                    i = ruaSemSaidaOP(lista, v, visitados)
                    if f"{v}, {i}" not in visitados and f"{i}, {v}" not in visitados:
                        casas = matriz[v][i]
                        matriz[v][i] -= casas
                        matriz[i][v] -= casas
                        visitados.append(f"{v}, {i}")
                        visitados.append(f"{i}, {v}")
                        conhecidos.append(f"{v}, {i}")
                        conhecidos.append(f"{i}, {v}")
                        time.sleep(casas / 100)
                        if f"{v}, {adj}" not in visitados and f"{adj}, {v}" not in visitados:
                            casas = matriz[v][adj]
                            matriz[v][adj] -= casas
                            matriz[adj][v] -= casas
                            visitados.append(f"{v}, {adj}")
                            conhecidos.append(f"{v}, {adj}")
                            time.sleep(casas / 100)
                            ColetaDados2(matriz, adj, lista, visitados, conhecidos, V)
                            visitados.append(f"{adj}, {v}")
                            conhecidos.append(f"{adj}, {v}")
            else:
                casas = matriz[v][adj]
                matriz[v][adj] -= casas
                matriz[adj][v] -= casas
                visitados.append(f"{v}, {adj}")
                conhecidos.append(f"{v}, {adj}")
    if v == V[0]:
        print(conhecidos)


def ruaSemSaida(lista, v, visitados):
    for adj in lista[v]:
        if saida(lista, adj) and f"{v}, {adj}" not in visitados:
            return adj
    return v


def saida(lista, v):
    if len(lista[v]) == 1:
        return True
    return False


def verificaOutros(lista, v, visitados):
    contador = 0
    for i in lista[v]:
        if f"{v}, {i}" not in visitados and f"{i}, {v}" not in visitados:
            contador += 1
    if contador >= 2:
        return True
    return False


def valor(lista, v, visitados):
    volta = 0
    for i in lista[v]:
        if f"{v}, {i}" not in visitados and f"{i}, {v}" not in visitados:
            volta += 1
            if volta == 2:
                return i


def ruaSemSaidaOP(lista, v, visitados):
    for adj in lista[v]:
        if saidaOP(lista, adj) and f"{v}, {adj}" not in visitados:
            return adj
    return v


def saidaOP(lista, v):
    if len(lista[v]) == 1:
        return True
    return False
