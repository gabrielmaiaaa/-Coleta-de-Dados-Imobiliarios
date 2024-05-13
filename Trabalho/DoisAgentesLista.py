import time
import numpy as np
import sys


def ColetaDados1(matriz, matrizCaminho, v, lista, visitadosCompartilhados, listaCompartilhada, conferir, visitados=None,
                 tempo_por_casa=None,
                 tempo_casas_e_ruas=None, distancia=None, qtd_ruas_repetidas=None, V=None):
    if visitados is None:
        visitados = []
        tempo_por_casa = [0]
        tempo_casas_e_ruas = [0]
        distancia = [0]
        qtd_ruas_repetidas = [0]
        V = [v]
    for adj in lista[v]:
        if f"{v}, {adj}" not in visitadosCompartilhados and f"{adj}, {v}" not in visitadosCompartilhados:
            if adj != V[0]:
                if ruaSemSaida(listaCompartilhada, v, visitadosCompartilhados) == v:
                    casas = matriz[v][adj]
                    matriz[v][adj] -= casas
                    matriz[adj][v] -= casas
                    visitadosCompartilhados.append(f"{v}, {adj}")
                    visitados.append(f"{v}, {adj}")
                    listaCompartilhada[v].remove(adj)
                    listaCompartilhada[adj].remove(v)
                    tempo_por_casa[0] += casas
                    tempo_casas_e_ruas[0] += casas + 2
                    distancia[0] += 70
                    time.sleep(casas / 100)
                    ColetaDados1(matriz, matrizCaminho, adj, lista, visitadosCompartilhados, listaCompartilhada,
                                 conferir, visitados,
                                 tempo_por_casa, tempo_casas_e_ruas, distancia, qtd_ruas_repetidas, V)
                    visitadosCompartilhados.append(f"{adj}, {v}")
                    visitados.append(f"{adj}, {v}")
                    tempo_casas_e_ruas[0] += 2
                    distancia[0] += 70
                    qtd_ruas_repetidas[0] += 1
                else:
                    i = ruaSemSaida(listaCompartilhada, v, visitadosCompartilhados)
                    if f"{v}, {i}" not in visitados and f"{i}, {v}" not in visitados:
                        casas = matriz[v][i]
                        matriz[v][i] -= casas
                        matriz[i][v] -= casas
                        visitadosCompartilhados.append(f"{v}, {i}")
                        visitadosCompartilhados.append(f"{i}, {v}")
                        visitados.append(f"{v}, {i}")
                        listaCompartilhada[v].remove(i)
                        tempo_por_casa[0] += casas
                        tempo_casas_e_ruas[0] += casas + 2
                        distancia[0] += 70
                        visitados.append(f"{i}, {v}")
                        listaCompartilhada[i].remove(v)
                        tempo_casas_e_ruas[0] += 2
                        distancia[0] += 70
                        time.sleep(casas / 100)
                        if f"{v}, {adj}" not in visitadosCompartilhados and f"{adj}, {v}" not in visitadosCompartilhados:
                            casas = matriz[v][adj]
                            matriz[v][adj] -= casas
                            matriz[adj][v] -= casas
                            visitadosCompartilhados.append(f"{v}, {adj}")
                            visitados.append(f"{v}, {adj}")
                            listaCompartilhada[v].remove(adj)
                            listaCompartilhada[adj].remove(v)
                            tempo_por_casa[0] += casas
                            tempo_casas_e_ruas[0] += casas + 2
                            distancia[0] += 70
                            time.sleep(casas / 100)
                            ColetaDados1(matriz, matrizCaminho, adj, lista, visitadosCompartilhados, listaCompartilhada,
                                         conferir, visitados,
                                         tempo_por_casa, tempo_casas_e_ruas, distancia, qtd_ruas_repetidas, V)
                            visitadosCompartilhados.append(f"{adj}, {v}")
                            visitados.append(f"{adj}, {v}")
                            distancia[0] += 70
                            tempo_casas_e_ruas[0] += 2
                            qtd_ruas_repetidas[0] += 1
            # elif adj == V[0] and verificaOutros(lista, v, visitadosCompartilhados):
            #     j = valor(lista, v, visitadosCompartilhados)
            #     casas = matriz[v][j]
            #     matriz[v][j] -= casas
            #     matriz[j][v] -= casas
            #     visitadosCompartilhados.append(f"{v}, {j}")
            #     visitados.append(f"{v}, {j}")
            #     listaCompartilhada[v].remove(j)
            #     listaCompartilhada[j].remove(v)
            #     tempo_por_casa[0] += casas
            #     tempo_casas_e_ruas[0] += casas + 2
            #     distancia[0] += 70
            #     time.sleep(casas / 100)
            #     ColetaDados1(matriz, matrizCaminho, j, lista, visitadosCompartilhados, listaCompartilhada, conferir,
            #                  visitados,
            #                  tempo_por_casa, tempo_casas_e_ruas, distancia, qtd_ruas_repetidas, V)
            #     # visitadosCompartilhados.append(f"{j}, {v}")
            #     # visitados.append(f"{j}, {v}")
            #     # distancia[0] += 70
            #     # tempo_casas_e_ruas[0] += 2
            #     # qtd_ruas_repetidas[0] += 1
            #     if f"{v}, {adj}" not in visitadosCompartilhados and f"{adj}, {v}" not in visitadosCompartilhados:
            #         casas = matriz[v][adj]
            #         matriz[v][adj] -= casas
            #         matriz[adj][v] -= casas
            #         visitadosCompartilhados.append(f"{v}, {adj}")
            #         visitados.append(f"{v}, {adj}")
            #         listaCompartilhada[v].remove(adj)
            #         listaCompartilhada[adj].remove(v)
            #         tempo_por_casa[0] += casas
            #         tempo_casas_e_ruas[0] += casas + 2
            #         distancia[0] += 70
    if verificaSeAcabou(matrizCaminho, listaCompartilhada, visitados, v, V, conferir, distancia, tempo_casas_e_ruas, qtd_ruas_repetidas):
        print("Agente Bond:")
        print(visitados)
        print(tempo_por_casa, tempo_casas_e_ruas, distancia, qtd_ruas_repetidas)
    # if v == V[0]:
    #
    #     # print()
        # print(visitadosCompartilhados)
        # print()
        # np.savetxt(f"Resultado/Bonde.txt", matriz, fmt="%d")
#
# def verificaOutros(lista, v, visitadosCompartilhados):
#     contador = 0
#     for i in lista[v]:
#         if f"{v}, {i}" not in visitadosCompartilhados and f"{i}, {v}" not in visitadosCompartilhados:
#             contador += 1
#     if contador >= 2:
#         return True
#     return False
#
#
# def valor(lista, v, visitadosCompartilhados):
#     volta = 0
#     for i in lista[v]:
#         if f"{v}, {i}" not in visitadosCompartilhados and f"{i}, {v}" not in visitadosCompartilhados:
#             volta += 1
#             if volta == 2:
#                 return i


def ColetaDados2(matriz, matrizCaminho, v, lista, visitadosCompartilhados, listaCompartilhada, conferir, visitados=None,
                 tempo_por_casa=None,
                 tempo_casas_e_ruas=None, distancia=None, qtd_ruas_repetidas=None, V=None):
    if visitados is None:
        visitados = []
        tempo_por_casa = [0]
        tempo_casas_e_ruas = [0]
        distancia = [0]
        qtd_ruas_repetidas = [0]
        V = [v]
    for adj in lista[v]:
        if f"{v}, {adj}" not in visitadosCompartilhados and f"{adj}, {v}" not in visitadosCompartilhados:
            if adj != V[0]:
                if ruaSemSaida(listaCompartilhada, v, visitadosCompartilhados) == v:
                    casas = matriz[v][adj]
                    matriz[v][adj] -= casas
                    matriz[adj][v] -= casas
                    visitadosCompartilhados.append(f"{v}, {adj}")
                    visitados.append(f"{v}, {adj}")
                    listaCompartilhada[v].remove(adj)
                    listaCompartilhada[adj].remove(v)
                    tempo_por_casa[0] += casas
                    tempo_casas_e_ruas[0] += casas + 2
                    distancia[0] += 70
                    time.sleep(casas / 100)
                    ColetaDados2(matriz, matrizCaminho, adj, lista, visitadosCompartilhados, listaCompartilhada,
                                 conferir, visitados,
                                 tempo_por_casa, tempo_casas_e_ruas, distancia, qtd_ruas_repetidas, V)
                    visitadosCompartilhados.append(f"{adj}, {v}")
                    visitados.append(f"{adj}, {v}")
                    distancia[0] += 70
                    tempo_casas_e_ruas[0] += 2
                    qtd_ruas_repetidas[0] += 1
                else:
                    i = ruaSemSaida(listaCompartilhada, v, visitadosCompartilhados)
                    if f"{v}, {i}" not in visitados and f"{i}, {v}" not in visitados:
                        casas = matriz[v][i]
                        matriz[v][i] -= casas
                        matriz[i][v] -= casas
                        visitadosCompartilhados.append(f"{v}, {i}")
                        visitadosCompartilhados.append(f"{i}, {v}")
                        visitados.append(f"{v}, {i}")
                        listaCompartilhada[v].remove(i)
                        tempo_por_casa[0] += casas
                        tempo_casas_e_ruas[0] += casas + 2
                        distancia[0] += 70
                        visitados.append(f"{i}, {v}")
                        listaCompartilhada[i].remove(v)
                        tempo_casas_e_ruas[0] += 2
                        distancia[0] += 70
                        time.sleep(casas / 100)
                        if f"{v}, {adj}" not in visitadosCompartilhados and f"{adj}, {v}" not in visitadosCompartilhados:
                            casas = matriz[v][adj]
                            matriz[v][adj] -= casas
                            matriz[adj][v] -= casas
                            visitadosCompartilhados.append(f"{v}, {adj}")
                            visitados.append(f"{v}, {adj}")
                            listaCompartilhada[v].remove(adj)
                            listaCompartilhada[adj].remove(v)
                            tempo_por_casa[0] += casas
                            tempo_casas_e_ruas[0] += casas + 2
                            distancia[0] += 70
                            time.sleep(casas / 100)
                            ColetaDados2(matriz, matrizCaminho, adj, lista, visitadosCompartilhados, listaCompartilhada,
                                         conferir, visitados,
                                         tempo_por_casa, tempo_casas_e_ruas, distancia, qtd_ruas_repetidas, V)
                            visitadosCompartilhados.append(f"{adj}, {v}")
                            visitados.append(f"{adj}, {v}")
                            distancia[0] += 70
                            tempo_casas_e_ruas[0] += 2
                            qtd_ruas_repetidas[0] += 1
            else:
                casas = matriz[v][adj]
                matriz[v][adj] -= casas
                matriz[adj][v] -= casas
                visitadosCompartilhados.append(f"{v}, {adj}")
                visitados.append(f"{v}, {adj}")
                listaCompartilhada[v].remove(adj)
                listaCompartilhada[adj].remove(v)
                tempo_por_casa[0] += casas
                tempo_casas_e_ruas[0] += casas + 2
                distancia[0] += 70
    if verificaSeAcabouOP(matrizCaminho, listaCompartilhada, visitados, v, V, conferir, distancia, tempo_casas_e_ruas, qtd_ruas_repetidas):
        print("Agente James:")
        print(visitados)
        print(tempo_por_casa, tempo_casas_e_ruas, distancia, qtd_ruas_repetidas)
    # if v == V[0]:
    #
        # print()
        # print(visitadosCompartilhados)
        # print()
        # np.savetxt(f"Resultado/James.txt", matriz, fmt="%d")


def ruaSemSaida(lista, v, visitados):
    for adj in lista[v]:
        if saida(lista, adj, visitados, v) and f"{v}, {adj}" not in visitados:
            return adj
    return v


def saida(lista, adj, visitados, v):
    if len(lista[adj]) == 1:
        return True
    return False


def verificaSeAcabou(matriz, listaCompartilhada, visitados, v, V, conferir, distancia, tempo_casas_e_ruas, qtd_ruas_repetidas):
    if all(not lista for lista in listaCompartilhada.values()) and (conferir[0] == 0 or conferir[0] == 2):
        percorrerInicio(matriz, visitados, v, V, conferir, distancia, tempo_casas_e_ruas, qtd_ruas_repetidas)
        return True
    else:
        return False


def percorrerInicio(matriz, visitado, vOrigem, vDestino, conferir, distancia, tempo_casas_e_ruas, qtd_ruas_repetidas):
    num_vertices = len(matriz)
    visitados = [False] * num_vertices
    distancias = [sys.maxsize] * num_vertices
    distancias[vOrigem] = 0
    rota = [-1] * num_vertices

    for _ in range(num_vertices):
        u = encontrar_vertice_minimo(distancias, visitados)
        visitados[u] = True

        if u == vDestino[0]:
            break

        for v in range(num_vertices):
            if (matriz[u][v] > 0 and not visitados[v] and
                    distancias[u] + matriz[u][v] < distancias[v]):
                distancias[v] = distancias[u] + matriz[u][v]
                rota[v] = u

    if rota[vDestino[0]] == -1:
        return [], float('inf')  # Não há caminho até o destino

    caminho = construir_caminho(rota, vOrigem, vDestino[0])
    for i in range(len(caminho) - 1):
        visitado.append(f"{caminho[i]}, {caminho[i + 1]}")
    # return print(caminho, distancias[vDestino[0]])
    distancia[0] += distancias[vDestino[0]]
    tempo_casas_e_ruas[0] += len(caminho)-1 * 2
    qtd_ruas_repetidas[0] += len(caminho)-1 * 1
    conferir[0] = 1


def encontrar_vertice_minimo(distancias, visitados):
    min_distancia = sys.maxsize
    min_vertice = -1

    for v in range(len(distancias)):
        if not visitados[v] and distancias[v] < min_distancia:
            min_distancia = distancias[v]
            min_vertice = v

    return min_vertice


def construir_caminho(rota, vOrigem, vDestino):
    caminho = []
    vertice = vDestino
    while vertice != vOrigem:
        caminho.append(vertice)
        vertice = rota[vertice]
    caminho.append(vOrigem)
    caminho.reverse()
    return caminho


def verificaSeAcabouOP(matriz, listaCompartilhada, visitados, v, V, conferir, distancia, tempo_casas_e_ruas, qtd_ruas_repetidas):
    if all(not lista for lista in listaCompartilhada.values()) and (conferir[0] == 0 or conferir[0] == 1):
        percorrerInicioOP(matriz, visitados, v, V, conferir, distancia, tempo_casas_e_ruas, qtd_ruas_repetidas)
        return True
    else:
        return False


def percorrerInicioOP(matriz, visitado, vOrigem, vDestino, conferir, distancia, tempo_casas_e_ruas, qtd_ruas_repetidas):
    num_vertices = len(matriz)
    visitados = [False] * num_vertices
    distancias = [sys.maxsize] * num_vertices
    distancias[vOrigem] = 0
    rota = [-1] * num_vertices

    for _ in range(num_vertices):
        u = encontrar_vertice_minimo(distancias, visitados)
        visitados[u] = True

        if u == vDestino[0]:
            break

        for v in range(num_vertices):
            if (matriz[u][v] > 0 and not visitados[v] and
                    distancias[u] + matriz[u][v] < distancias[v]):
                distancias[v] = distancias[u] + matriz[u][v]
                rota[v] = u

    if rota[vDestino[0]] == -1:
        return [], float('inf')  # Não há caminho até o destino

    caminho = construir_caminho(rota, vOrigem, vDestino[0])
    for i in range(len(caminho) - 1):
        visitado.append(f"{caminho[i]}, {caminho[i + 1]}")
    # return print(caminho, distancias[vDestino[0]])
    distancia[0] += distancias[vDestino[0]]
    tempo_casas_e_ruas[0] += len(caminho)-1 * 2
    qtd_ruas_repetidas[0] += len(caminho)-1 * 1
    conferir[0] = 2
