# ''' importa a biblioteca das funções '''
from Matriz_Metodos import matriz_dataset as ds
from Listas_Metodos import listas_caracteristicas as lista
from Trabalho import UmAgente as um, DoisAgentes as dois
import time
import threading

matriz = ds.criarMatriz("Eloi Mendes")
matrizCaminho = ds.criarMatriz("Eloi Mendes Distancias")
listaCompartilhada = lista.criaListaAdjacencias(matriz)
listaAdjCrescente = lista.criaListaAdjacencias(matriz)
listaAdjDecrescente = lista.listaAdjacneteInversa(matriz)
listaAux = lista.listaAdjacneteInversa(matriz)

opcao = int(input("Escolha se você quer com um agente ou com dois\n"
                  "1 para um agente\n"
                  "2 para dois agentes\n"))

if opcao == 1:
    print("Caso com um agente")
    inicioUm = time.time()

    um.Agente0(matriz, matrizCaminho, listaAdjDecrescente, listaAux, 0)

    fimUm = time.time()
    tempoUm = fimUm - inicioUm
    print("Tempo de execução")
    print(tempoUm)
elif opcao == 2:
    print("Caso com dois agentes")
    inicioDois = time.time()
    visitados = []
    conferir = [0]
    PrimeiroAgente = threading.Thread(target=dois.Agente1, args=(matriz, matrizCaminho, 0, listaAdjDecrescente,
                                                                 visitados, listaCompartilhada, conferir))
    SegundoAgente = threading.Thread(target=dois.Agente2, args=(matriz, matrizCaminho, 0, listaAdjDecrescente,
                                                                visitados, listaCompartilhada, conferir))
    PrimeiroAgente.start()
    SegundoAgente.start()

    PrimeiroAgente.join()
    SegundoAgente.join()

    fimDois = time.time()
    tempoDois = fimDois - inicioDois
    print("Tempo de execução")
    print(tempoDois)
else:
    print("Ópção inválida")
