import numpy as np
import igraph as ig
import cairo
import matplotlib.pyplot as plt
import networkx as nx


def ColetaDeDados(matriz, matrizCaminho, lista, listaAux, v, visitados=None, tempo_por_casa=None, tempo_casas_e_ruas=None,
                  distancia=None, qtd_ruas_repetidas=None, V=None, grafo=None, conferir=None):
    if visitados is None:
        visitados = []
        tempo_por_casa = [0]
        tempo_casas_e_ruas = [0]
        distancia = [0]
        qtd_ruas_repetidas = [0]
        V = [v]
        conferir = [0]
        # grafo = nx.Graph()
    for adj in lista[v]:
        if (v, adj) not in visitados and (adj, v) not in visitados:
            if adj != V[0]:
                if ruaSemSaida(listaAux, v, visitados) == v:
                    visitados.append((v, adj))
                    listaAux[v].remove(adj)
                    listaAux[adj].remove(v)
                    tempo_por_casa[0] += matriz[v][adj]
                    tempo_casas_e_ruas[0] += matriz[v][adj] + 2
                    distancia[0] += matrizCaminho[v][adj]
                    ColetaDeDados(matriz, matrizCaminho, lista, listaAux, adj, visitados, tempo_por_casa,
                                  tempo_casas_e_ruas, distancia, qtd_ruas_repetidas, V, grafo, conferir)
                    # print((v, adj))
                    visitados.append((adj, v))
                    tempo_casas_e_ruas[0] += 2
                    distancia[0] += matrizCaminho[adj][v]
                    qtd_ruas_repetidas[0] += 1
                else:
                    i = ruaSemSaida(listaAux, v, visitados)
                    if (v, i) not in visitados and (i, v) not in visitados:
                        visitados.append((v, i))
                        listaAux[v].remove(i)
                        tempo_por_casa[0] += matriz[v][i]
                        tempo_casas_e_ruas[0] += matriz[v][i] + 2
                        distancia[0] += matrizCaminho[v][i]
                        visitados.append((i, v))
                        listaAux[i].remove(v)
                        tempo_casas_e_ruas[0] += 2
                        distancia[0] += matrizCaminho[i][v]
                        if (v, adj) not in visitados and (adj, v) not in visitados:
                            visitados.append((v, adj))
                            listaAux[v].remove(adj)
                            listaAux[adj].remove(v)
                            tempo_por_casa[0] += matriz[v][adj]
                            tempo_casas_e_ruas[0] += matriz[v][adj] + 2
                            distancia[0] += matrizCaminho[v][adj]
                            ColetaDeDados(matriz, matrizCaminho, lista, listaAux, adj, visitados, tempo_por_casa,
                                          tempo_casas_e_ruas, distancia, qtd_ruas_repetidas, V, grafo, conferir)
                            # print((v, adj))
                            visitados.append((adj, v))
                            tempo_casas_e_ruas[0] += 2
                            distancia[0] += matrizCaminho[adj][v]
                            qtd_ruas_repetidas[0] += 1
            else:
                visitados.append((v, adj))
                tempo_por_casa[0] += matriz[v][adj]
                tempo_casas_e_ruas[0] += matriz[v][adj] + 2
                distancia[0] += matrizCaminho[v][adj]
                contador = 0
                for elemento in visitados:
                    invertido = elemento[::-1]
                    if invertido in visitados:
                        contador += 1
                print(contador)
                print(len(visitados))
                print(visitados)
                print(tempo_por_casa, tempo_casas_e_ruas, distancia, qtd_ruas_repetidas)
                # grafo.add_edges_from(visitados)
                # nx.draw(grafo, with_labels=True, node_color='lightblue', edge_color='gray')
                # ig.plot(grafo)
                # plt.savefig("grafo.png")
                # plt.show()
    if verificaSeAcabou(matriz, listaAux, visitados, v, V, conferir, distancia, tempo_casas_e_ruas, qtd_ruas_repetidas):
        print(visitados)
        print(tempo_por_casa, tempo_casas_e_ruas, distancia, qtd_ruas_repetidas)
        # grafo.add_edges_from(visitados)
        # nx.draw(grafo, with_labels=True, node_color='lightblue', edge_color='gray')
        # ig.plot(grafo)
        # plt.savefig("grafo1.png")
        # plt.show()


def ruaSemSaida(lista, v, visitados):
    for adj in lista[v]:
        if saida(lista, adj) and (v, adj) not in visitados:
            return adj
    return v


def saida(lista, v):
    if len(lista[v]) == 1:
        return True
    return False

def verificaSeAcabou(matrizCaminho, listaCompartilhada, visitados, v, V, conferir, distancia, tempo_casas_e_ruas, qtd_ruas_repetidas):
    if all(not lista for lista in listaCompartilhada.values()) and conferir[0] == 0:
        dijkstra(matrizCaminho, visitados, v, V, conferir, distancia, tempo_casas_e_ruas, qtd_ruas_repetidas)
        return True
    else:
        return False


def dijkstra(matrizCaminho, visitado, vOrigem, vDestino, conferir, distancia, tempo_casas_e_ruas, qtd_ruas_repetidas):
    custo = [float('inf')] * len(matrizCaminho)
    rota = [0] * len(matrizCaminho)
    custo[vOrigem] = 0
    F = []
    N = set(range(len(matrizCaminho)))
    while N:
        v = min(N, key=lambda v: custo[v])
        if v == vDestino[0]:
            break
        F.append(v)
        N.remove(v)
        for u in range(len(matrizCaminho)):
            if matrizCaminho[v][u] != 0 and custo[v] + matrizCaminho[v][u] < custo[u]:
                custo[u] = custo[v] + matrizCaminho[v][u]
                rota[u] = v
    verdadeiraRota = [vDestino[0]]
    verticeAtual = vDestino[0]
    while verticeAtual != vOrigem:
        verticeAtual = rota[verticeAtual]
        verdadeiraRota.insert(0, verticeAtual)
    diferencaCusto = custo[vDestino[0]] - custo[vOrigem]
    for i in range(len(verdadeiraRota) - 1):
        visitado.append((verdadeiraRota[i], verdadeiraRota[i + 1]))
    distancia[0] += diferencaCusto
    tempo_casas_e_ruas[0] += len(verdadeiraRota) - 1 * 2
    qtd_ruas_repetidas[0] += len(verdadeiraRota) - 1
    conferir[0] = 1
