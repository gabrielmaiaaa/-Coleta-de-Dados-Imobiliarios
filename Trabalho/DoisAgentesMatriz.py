import time
import numpy as np


def ColetaDados1(matriz, v, foi, visitados=None, totalCasas=None, V=None, p=None):
    if visitados is None:
        visitados = []
        totalCasas = [0]  # variavel usada para calcular a quantidade de casas visitadas
        V = [v]
    for adj in range(len(matriz)):
        if matriz[v][adj] > -1 and f"{v}, {adj}" not in visitados and f"{adj}, {v}" not in visitados:
            if adj != V[0]:
                if ruaSemSaida(matriz, v, visitados) == v:
                    if matriz[v][adj] == 0 and AlemDoZero(matriz, v, visitados):
                        i = valorAlemDoZero(matriz, v, visitados)
                        if f"{v}, {i}" not in visitados and f"{i}, {v}" not in visitados:
                            casas = matriz[v][i]
                            # print(v, i)
                            # print(totalCasas[0], casas)
                            matriz[v][i] -= casas
                            matriz[i][v] -= casas
                            visitados.append(f"{v}, {i}")  # coloca o conjunto de arestas como visitados
                            totalCasas[0] += casas
                            time.sleep(casas / 100)
                            ColetaDados1(matriz, i, foi, visitados, totalCasas, V, p)
                            # visitados.append(f"{i}, {v}")
                            if f"{v}, {adj}" not in visitados and f"{adj}, {v}" not in visitados:
                                casas = matriz[v][adj]
                                # print(v, adj)
                                # print(totalCasas[0], casas)
                                matriz[v][adj] -= casas
                                matriz[adj][v] -= casas
                                visitados.append(f"{v}, {adj}")  # coloca o conjunto de arestas como visitados
                                totalCasas[0] += casas
                                time.sleep(casas / 100)
                                ColetaDados1(matriz, adj, foi, visitados, totalCasas, V,
                                             p)  # chama recursivamente para visitar os próximos
                                # visitados.append(f"{adj}, {v}")
                    else:
                        casas = matriz[v][adj]
                        # print(v, adj)
                        # print(totalCasas[0], casas)
                        matriz[v][adj] -= casas
                        matriz[adj][v] -= casas
                        visitados.append(f"{v}, {adj}")  # coloca o conjunto de arestas como visitados
                        totalCasas[0] += casas

                        time.sleep(casas / 100)
                        ColetaDados1(matriz, adj, foi, visitados, totalCasas, V,
                                     p)  # chama recursivamente para visitar os próximos
                        # visitados.append(f"{adj}, {v}")
                else:
                    i = ruaSemSaida(matriz, v, visitados)
                    if f"{v}, {i}" not in visitados and f"{i}, {v}" not in visitados:
                        casas = matriz[v][i]
                        # print(v, i)
                        # print(totalCasas[0], casas)
                        matriz[v][i] -= casas
                        matriz[i][v] -= casas
                        visitados.append(f"{v}, {i}")  # coloca o conjunto de arestas como visitados
                        visitados.append(f"{i}, {v}")  # coloca o conjunto de arestas como visitados
                        totalCasas[0] += casas

                        time.sleep(casas / 100)
                        if f"{v}, {adj}" not in visitados and f"{adj}, {v}" not in visitados:
                            casas = matriz[v][adj]
                            # print(v, adj)
                            # print(totalCasas[0], casas)
                            matriz[v][adj] -= casas
                            matriz[adj][v] -= casas
                            visitados.append(f"{v}, {adj}")  # coloca o conjunto de arestas como visitados
                            totalCasas[0] += casas
                            time.sleep(casas / 100)
                            ColetaDados1(matriz, adj, foi, visitados, totalCasas, V,
                                         p)  # chama recursivamente para visitar os próximos
                            # visitados.append(f"{adj}, {v}")

            elif adj == V[0] and verificaOutros(matriz, v, visitados):
                j = valor(matriz, v, visitados)
                casas = matriz[v][j]
                matriz[v][j] -= casas
                matriz[j][v] -= casas
                visitados.append(f"{v}, {j}")  # coloca o conjunto de arestas como visitados
                totalCasas[0] += casas

                time.sleep(casas / 100)
                ColetaDados1(matriz, j, foi, visitados, totalCasas, V,
                             p)  # chama recursivamente para visitar os próximos
                visitados.append(f"{j}, {v}")
                if f"{v}, {adj}" not in visitados and f"{adj}, {v}" not in visitados:
                    casas = matriz[v][adj]
                    # print(v, adj)
                    # print(totalCasas[0], casas)
                    matriz[v][adj] -= casas
                    matriz[adj][v] -= casas
                    visitados.append(f"{v}, {adj}")  # coloca o conjunto de arestas como visitados
                    p = adj
                    totalCasas[0] += casas
    if p == V[0]:
        print("Agente Bond:")
        print(visitados, totalCasas)
        np.savetxt(f"Resultado/Bonde.txt", matriz, fmt="%d")
        # for i in range(len(matriz)):
        #     for j in range(len(matriz)):
        #         if matriz[i][j] > 0:
        #             print(f"{i}, {j} - {matriz[i][j]}  {matriz[j][i]}")


def verificaOutros(matriz, v, visitados):
    contador = 0
    for i in range(len(matriz)):
        if matriz[v][i] > -1 and f"{v}, {i}" not in visitados and f"{i}, {v}" not in visitados:
            contador += 1
    if contador >= 2:
        return True
    return False


def valor(matriz, v, visitados):
    volta = 0
    for i in range(len(matriz)):
        if matriz[v][i] > -1 and f"{v}, {i}" not in visitados and f"{i}, {v}" not in visitados:
            volta += 1
            if volta == 2:
                return i


def ruaSemSaida(matriz, v, visitados):
    for adj in range(len(matriz)):
        if matriz[v][adj] > -1 and saida(matriz, adj) and f"{v}, {adj}" not in visitados:
            return adj
    return v


def saida(matriz, v):
    nao = 0
    for adj in range(len(matriz)):
        if matriz[v][adj] == -1:
            nao += 1
    if len(matriz) - 1 == nao:
        return True
    return False


def AlemDoZero(matriz, v, visitados):
    for adj in range(len(matriz)):
        if matriz[v][adj] > 0 and f"{v}, {adj}" not in visitados and f"{adj}, {v}" not in visitados:
            return True
    return False


def valorAlemDoZero(matriz, v, visitados):
    for i in range(len(matriz)):
        if matriz[v][i] > 0 and f"{v}, {i}" not in visitados and f"{i}, {v}" not in visitados:
            return i


def ColetaDados2(matriz, v, foi, visitados=None, totalCasas=None, V=None, p=None):
    if visitados is None:
        visitados = []
        totalCasas = [0]  # variavel usada para calcular a quantidade de casas visitadas
        V = [v]
    for adj in range(len(matriz) - 1, -1, -1):
        if matriz[v][adj] > -1 and f"{v}, {adj}" not in visitados and f"{adj}, {v}" not in visitados:
            if adj != V[0]:
                if ruaSemSaidaOP(matriz, v, visitados) == v:
                    if matriz[v][adj] == 0 and AlemDoZeroOP(matriz, v, visitados):
                        i = valorAlemDoZeroOP(matriz, v, visitados)
                        if f"{v}, {i}" not in visitados and f"{i}, {v}" not in visitados:
                            casas = matriz[v][i]
                            # print(v, i)
                            # print(totalCasas[0], casas)
                            matriz[v][i] -= casas
                            matriz[i][v] -= casas
                            visitados.append(f"{v}, {i}")  # coloca o conjunto de arestas como visitados
                            totalCasas[0] += casas

                            time.sleep(casas / 100)
                            ColetaDados2(matriz, i, foi, visitados, totalCasas, V, p)
                            visitados.append(f"{i}, {v}")
                            if f"{v}, {adj}" not in visitados and f"{adj}, {v}" not in visitados:
                                casas = matriz[v][adj]
                                # print(v, adj)
                                # print(totalCasas[0], casas)
                                matriz[v][adj] -= casas
                                matriz[adj][v] -= casas
                                visitados.append(f"{v}, {adj}")  # coloca o conjunto de arestas como visitados
                                totalCasas[0] += casas
                                time.sleep(casas / 100)
                                ColetaDados2(matriz, adj, foi, visitados, totalCasas, V,
                                             p)  # chama recursivamente para visitar os próximos
                                # visitados.append(f"{adj}, {v}")

                    else:
                        casas = matriz[v][adj]
                        # print(v, adj)
                        # print(totalCasas[0], casas)
                        matriz[v][adj] -= casas
                        matriz[adj][v] -= casas
                        visitados.append(f"{v}, {adj}")  # coloca o conjunto de arestas como visitados
                        totalCasas[0] += casas
                        time.sleep(casas / 100)
                        ColetaDados2(matriz, adj, foi, visitados, totalCasas, V,
                                     p)  # chama recursivamente para visitar os próximos
                        # visitados.append(f"{adj}, {v}")

                else:
                    i = ruaSemSaidaOP(matriz, v, visitados)
                    if f"{v}, {i}" not in visitados and f"{i}, {v}" not in visitados:
                        casas = matriz[v][i]
                        # print(v, i)
                        # print(totalCasas[0], casas)
                        matriz[v][i] -= casas
                        matriz[i][v] -= casas
                        visitados.append(f"{v}, {i}")  # coloca o conjunto de arestas como visitados
                        visitados.append(f"{i}, {v}")  # coloca o conjunto de arestas como visitados
                        totalCasas[0] += casas
                        time.sleep(casas / 100)

                        if f"{v}, {adj}" not in visitados and f"{adj}, {v}" not in visitados:
                            casas = matriz[v][adj]
                            # print(v, adj)
                            # print(totalCasas[0], casas)
                            matriz[v][adj] -= casas
                            matriz[adj][v] -= casas
                            visitados.append(f"{v}, {adj}")  # coloca o conjunto de arestas como visitados
                            totalCasas[0] += casas
                            time.sleep(casas / 100)
                            ColetaDados2(matriz, adj, foi, visitados, totalCasas, V,
                                         p)  # chama recursivamente para visitar os próximos
                            # visitados.append(f"{adj}, {v}")

            elif adj == V[0]:
                # and verificaOutrosOP(matriz, v, visitados):
                # j = valorOP(matriz, v, visitados)
                # casas = matriz[v][j]
                # matriz[v][j] -= casas
                # matriz[j][v] -= casas
                # visitados.append(f"{v}, {j}")  # coloca o conjunto de arestas como visitados
                # totalCasas[0] += casas
                # time.sleep(casas / 100)
                # ColetaDados2(matriz, j, foi, visitados,
                # totalCasas, V, p)  # chama recursivamente para visitar os próximos
                # visitados.append(f"{j}, {v}")
                # if f"{v}, {adj}" not in visitados and f"{adj}, {v}" not in visitados:
                casas = matriz[v][adj]
                # print(v, adj)
                # print(totalCasas[0], casas)
                matriz[v][adj] -= casas
                matriz[adj][v] -= casas
                visitados.append(f"{v}, {adj}")  # coloca o conjunto de arestas como visitados
                p = adj
                totalCasas[0] += casas
    if p == V[0]:
        print("Agente James:")
        print(visitados, totalCasas)
        np.savetxt(f"Resultado/James.txt", matriz, fmt="%d")
        # for i in range(len(matriz)):
        #     for j in range(len(matriz)):
        #         if matriz[i][j] > 0:
        #             print(f"{i}, {j} - {matriz[i][j]}  {matriz[j][i]}")


def verificaOutrosOP(matriz, v, visitados):
    contador = 0
    for i in range(len(matriz) - 1, -1, -1):
        if matriz[v][i] > -1 and f"{v}, {i}" not in visitados and f"{i}, {v}" not in visitados:
            contador += 1
    if contador >= 2:
        return True
    return False


def valorOP(matriz, v, visitados):
    volta = 0
    for i in range(len(matriz) - 1, -1, -1):
        if matriz[v][i] > -1 and f"{v}, {i}" not in visitados and f"{i}, {v}" not in visitados:
            volta += 1
            if volta == 2:
                return i


def ruaSemSaidaOP(matriz, v, visitados):
    for adj in range(len(matriz) - 1, -1, -1):
        if matriz[v][adj] > -1 and saidaOP(matriz, adj) and f"{v}, {adj}" not in visitados:
            return adj
    return v


def saidaOP(matriz, v):
    nao = 0
    for adj in range(len(matriz) - 1, -1, -1):
        if matriz[v][adj] == -1:
            nao += 1
    if len(matriz) - 1 == nao:
        return True
    return False


def AlemDoZeroOP(matriz, v, visitados):
    for adj in range(len(matriz) - 1, -1, -1):
        if matriz[v][adj] > 0 and f"{v}, {adj}" not in visitados and f"{adj}, {v}" not in visitados:
            return True
    return False


def valorAlemDoZeroOP(matriz, v, visitados):
    for i in range(len(matriz) - 1, -1, -1):
        if matriz[v][i] > 0 and f"{v}, {i}" not in visitados and f"{i}, {v}" not in visitados:
            return i
