import time
import igraph as ig
import matplotlib.pyplot as plt
import networkx as nx


def Agente1(matriz, matrizCaminho, v, lista, visitadosCompartilhados, listaCompartilhada, conferir, visitados=None,
                 tempo_por_casa=None, tempo_casas_e_ruas=None, distancia=None, qtd_ruas_repetidas=None, V=None,
                 grafo=None, confere=None):
    if visitados is None:
        visitados = []
        tempo_por_casa = [0]
        tempo_casas_e_ruas = [0]
        distancia = [0]
        qtd_ruas_repetidas = [0]
        V = [v]
        confere = [0]
        # grafo = nx.Graph()
    for adj in lista[v]:
        if (v, adj) not in visitadosCompartilhados and (adj, v) not in visitadosCompartilhados:
            if ruaSemSaida(listaCompartilhada, v, visitadosCompartilhados) == v:
                visitadosCompartilhados.append((v, adj))
                visitados.append((v, adj))
                listaCompartilhada[v].remove(adj)
                listaCompartilhada[adj].remove(v)
                tempo_por_casa[0] += matriz[v][adj]
                tempo_casas_e_ruas[0] += matriz[v][adj] + 2
                distancia[0] += matrizCaminho[v][adj]
                time.sleep(matriz[v][adj] / 1000)
                Agente1(matriz, matrizCaminho, adj, lista, visitadosCompartilhados, listaCompartilhada,
                             conferir, visitados, tempo_por_casa, tempo_casas_e_ruas, distancia, qtd_ruas_repetidas,
                             V, grafo, confere)
                visitadosCompartilhados.append((adj, v))
                visitados.append((adj, v))
                tempo_casas_e_ruas[0] += 2
                distancia[0] += matrizCaminho[adj][v]
                qtd_ruas_repetidas[0] += 1
            else:
                i = ruaSemSaida(listaCompartilhada, v, visitadosCompartilhados)
                visitadosCompartilhados.append((v, i))
                visitadosCompartilhados.append((i, v))
                visitados.append((v, i))
                listaCompartilhada[v].remove(i)
                tempo_por_casa[0] += matriz[v][i]
                tempo_casas_e_ruas[0] += matriz[v][i] + 2
                distancia[0] += matrizCaminho[v][i]
                visitados.append((i, v))
                listaCompartilhada[i].remove(v)
                tempo_casas_e_ruas[0] += 2
                distancia[0] += matrizCaminho[i][v]
                time.sleep(matriz[v][i] / 1000)
                if (v, adj) not in visitadosCompartilhados and (adj, v) not in visitadosCompartilhados:
                    visitadosCompartilhados.append((v, adj))
                    visitados.append((v, adj))
                    listaCompartilhada[v].remove(adj)
                    listaCompartilhada[adj].remove(v)
                    tempo_por_casa[0] += matriz[v][adj]
                    tempo_casas_e_ruas[0] += matriz[v][adj] + 2
                    distancia[0] += matrizCaminho[v][adj]
                    time.sleep(matriz[v][adj] / 1000)
                    Agente1(matriz, matrizCaminho, adj, lista, visitadosCompartilhados, listaCompartilhada,
                                 conferir, visitados, tempo_por_casa, tempo_casas_e_ruas, distancia,
                                 qtd_ruas_repetidas, V, grafo, confere)
                    visitadosCompartilhados.append((adj, v))
                    visitados.append((adj, v))
                    distancia[0] += matrizCaminho[adj][v]
                    tempo_casas_e_ruas[0] += 2
                    qtd_ruas_repetidas[0] += 1
    if outroVerticeBFS(lista, v, visitadosCompartilhados):
        i = outroVerticeBFS(lista, v, visitadosCompartilhados)
        dijkstra(matrizCaminho, visitados, v, i, distancia, tempo_casas_e_ruas, qtd_ruas_repetidas)
        Agente1(matriz, matrizCaminho, i, lista, visitadosCompartilhados, listaCompartilhada,
                     conferir, visitados, tempo_por_casa, tempo_casas_e_ruas, distancia, qtd_ruas_repetidas, V, grafo,
                     confere)
    if verificaSeAcabou1(matrizCaminho, listaCompartilhada, visitados, v, V, conferir, distancia, tempo_casas_e_ruas,
                        qtd_ruas_repetidas) and confere[0] == 0:
        print("Agente1")
        print(visitados)
        print(tempo_por_casa, tempo_casas_e_ruas, distancia, qtd_ruas_repetidas)
        confere[0] = 1
        # grafo.add_edges_from(visitados)
        # nx.draw(grafo, with_labels=True, node_color='lightblue', edge_color='gray')
        # plt.savefig("grafo1.png")
        # plt.show()


def Agente2(matriz, matrizCaminho, v, lista, visitadosCompartilhados, listaCompartilhada, conferir, visitados=None,
                 tempo_por_casa=None, tempo_casas_e_ruas=None, distancia=None, qtd_ruas_repetidas=None, V=None,
                 grafo=None, confere=None):
    if visitados is None:
        visitados = []
        tempo_por_casa = [0]
        tempo_casas_e_ruas = [0]
        distancia = [0]
        qtd_ruas_repetidas = [0]
        V = [v]
        confere = [0]
        # grafo = nx.Graph()
    for adj in lista[v]:
        if (v, adj) not in visitadosCompartilhados and (adj, v) not in visitadosCompartilhados:
            if ruaSemSaida(listaCompartilhada, v, visitadosCompartilhados) == v:
                visitadosCompartilhados.append((v, adj))
                visitados.append((v, adj))
                listaCompartilhada[v].remove(adj)
                listaCompartilhada[adj].remove(v)
                tempo_por_casa[0] += matriz[v][adj]
                tempo_casas_e_ruas[0] += matriz[v][adj] + 2
                distancia[0] += matrizCaminho[v][adj]
                time.sleep(matriz[v][adj] / 1000)
                Agente2(matriz, matrizCaminho, adj, lista, visitadosCompartilhados, listaCompartilhada,
                             conferir, visitados, tempo_por_casa, tempo_casas_e_ruas, distancia, qtd_ruas_repetidas,
                             V, grafo, confere)
                visitadosCompartilhados.append((adj, v))
                visitados.append((adj, v))
                distancia[0] += matrizCaminho[adj][v]
                tempo_casas_e_ruas[0] += 2
                qtd_ruas_repetidas[0] += 1
            else:
                i = ruaSemSaida(listaCompartilhada, v, visitadosCompartilhados)
                visitadosCompartilhados.append((v, i))
                visitadosCompartilhados.append((i, v))
                visitados.append((v, i))
                listaCompartilhada[v].remove(i)
                tempo_por_casa[0] += matriz[v][i]
                tempo_casas_e_ruas[0] += matriz[v][i] + 2
                distancia[0] += matrizCaminho[v][i]
                visitados.append((i, v))
                listaCompartilhada[i].remove(v)
                tempo_casas_e_ruas[0] += 2
                distancia[0] += matrizCaminho[i][v]
                time.sleep(matriz[v][i] / 1000)
                if (v, adj) not in visitadosCompartilhados and (adj, v) not in visitadosCompartilhados:
                    visitadosCompartilhados.append((v, adj))
                    visitados.append((v, adj))
                    listaCompartilhada[v].remove(adj)
                    listaCompartilhada[adj].remove(v)
                    tempo_por_casa[0] += matriz[v][adj]
                    tempo_casas_e_ruas[0] += matriz[v][adj] + 2
                    distancia[0] += matrizCaminho[v][adj]
                    time.sleep(matriz[v][adj] / 1000)
                    Agente2(matriz, matrizCaminho, adj, lista, visitadosCompartilhados, listaCompartilhada,
                                 conferir, visitados, tempo_por_casa, tempo_casas_e_ruas, distancia,
                                 qtd_ruas_repetidas, V, grafo, confere)
                    visitadosCompartilhados.append((adj, v))
                    visitados.append((adj, v))
                    distancia[0] += matrizCaminho[adj][v]
                    tempo_casas_e_ruas[0] += 2
                    qtd_ruas_repetidas[0] += 1
    if outroVerticeBFS(lista, v, visitadosCompartilhados):
        i = outroVerticeBFS(lista, v, visitadosCompartilhados)
        dijkstra(matrizCaminho, visitados, v, i, distancia, tempo_casas_e_ruas, qtd_ruas_repetidas)
        Agente2(matriz, matrizCaminho, i, lista, visitadosCompartilhados, listaCompartilhada,
                     conferir, visitados, tempo_por_casa, tempo_casas_e_ruas, distancia, qtd_ruas_repetidas, V, grafo,
                     confere)
    if verificaSeAcabou2(matrizCaminho, listaCompartilhada, visitados, v, V, conferir, distancia, tempo_casas_e_ruas,
                          qtd_ruas_repetidas) and confere[0] == 0:
        time.sleep(0.1)
        print("Agente2")
        print(visitados)
        print(tempo_por_casa, tempo_casas_e_ruas, distancia, qtd_ruas_repetidas)
        confere[0] = 1
        # grafo.add_edges_from(visitados)
        # nx.draw(grafo, with_labels=True, node_color='lightblue', edge_color='gray')
        # plt.savefig("grafo2.png")
        # plt.show()


def ruaSemSaida(lista, v, visitados):
    for adj in lista[v]:
        if saida(lista, adj) and (v, adj) not in visitados:
            return adj
    return v


def saida(lista, adj):
    if len(lista[adj]) == 1:
        return True
    return False


def verificaSeAcabou1(matrizCaminho, listaCompartilhada, visitados, v, V, conferir, distancia, tempo_casas_e_ruas,
                     qtd_ruas_repetidas):
    if all(not lista for lista in listaCompartilhada.values()) and (conferir[0] == 0 or conferir[0] == 2):
        dijkstra1(matrizCaminho, visitados, v, V, conferir, distancia, tempo_casas_e_ruas, qtd_ruas_repetidas)
        return True
    else:
        return False


def dijkstra1(matrizCaminho, visitado, vOrigem, vDestino, conferir, distancia, tempo_casas_e_ruas, qtd_ruas_repetidas):
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


def verificaSeAcabou2(matrizCaminho, listaCompartilhada, visitados, v, V, conferir, distancia, tempo_casas_e_ruas,
                       qtd_ruas_repetidas):
    if all(not lista for lista in listaCompartilhada.values()) and (conferir[0] == 0 or conferir[0] == 1):
        dijkstra2(matrizCaminho, visitados, v, V, conferir, distancia, tempo_casas_e_ruas, qtd_ruas_repetidas)
        return True
    else:
        return False


def dijkstra2(matrizCaminho, visitado, vOrigem, vDestino, conferir, distancia, tempo_casas_e_ruas, qtd_ruas_repetidas):
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
    conferir[0] = 2


def outroVerticeBFS(lista, v, visitadosCompartilhados):
    Q = [v]
    analisado = []
    while Q:
        v = Q.pop(0)
        for adj in lista[v]:
            if adj not in Q and adj not in analisado:
                Q.append(adj)
            if (v, adj) not in visitadosCompartilhados and (adj, v) not in visitadosCompartilhados:
                return v
        analisado.append(v)
    return False


def dijkstra(matrizCaminho, visitado, vOrigem, vDestino, distancia, tempo_casas_e_ruas, qtd_ruas_repetidas):
    custo = [float('inf')] * len(matrizCaminho)
    rota = [0] * len(matrizCaminho)
    custo[vOrigem] = 0
    F = []
    N = set(range(len(matrizCaminho)))
    while N:
        v = min(N, key=lambda v: custo[v])
        if v == vDestino:
            break
        F.append(v)
        N.remove(v)
        for u in range(len(matrizCaminho)):
            if matrizCaminho[v][u] != 0 and custo[v] + matrizCaminho[v][u] < custo[u]:
                custo[u] = custo[v] + matrizCaminho[v][u]
                rota[u] = v
    verdadeiraRota = [vDestino]
    verticeAtual = vDestino
    while verticeAtual != vOrigem:
        verticeAtual = rota[verticeAtual]
        verdadeiraRota.insert(0, verticeAtual)
    diferencaCusto = custo[vDestino] - custo[vOrigem]
    for i in range(len(verdadeiraRota) - 1):
        visitado.append((verdadeiraRota[i], verdadeiraRota[i + 1]))
    distancia[0] += diferencaCusto
    tempo_casas_e_ruas[0] += len(verdadeiraRota) - 1 * 2
    qtd_ruas_repetidas[0] += len(verdadeiraRota) - 1
