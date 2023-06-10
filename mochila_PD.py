import numpy as np
from itertools import combinations

def calcula_valor_mochila(mochila,objetos):
    """retorna a soma do valor dos objetos contidos na mochila"""
    valor = 0
    for i in mochila:
        valor += objetos[i][1]
    return valor

def calcula_peso_mochila(mochila, objetos):
    """retorna a soma do peso dos objetos contidos na mochila"""
    peso = 0
    for i in mochila:
        peso += objetos[i][0]
    return peso

def mochila_PD(K,V):
    """Recebe uma capacidade K e um vetor de tuplas (peso,valor), e retorna a melhor mochila"""

    #eu incremento o K em 1 por que a matriz tera K+1 colunas, visto que vai de 0 até K
    K=K+1

    n = len(V)
    mochilas = np.empty((n,K),dtype=object)

    #faz a primeira linha
    for j in range(K):
        if j < V[0][0]:
            mochilas[0][j] = []

        else:
            mochilas[0][j] = [0]

    #agora fazemos as outras linhas
    for i in range(1,n):
        for j in range(K):
            #se a mochilas nao tiver capacidade pro peso do objeto desta linha, simplesmente copia a mochilas anterior
            if j < V[i][0]:
                mochilas[i][j] = mochilas[i-1][j].copy()

            #se a mochilas tem capacidade, pega o maximo entre (nao levar o objeto, levar o objeto e somar com uma mochilas de capacidade menor)
            else:
                if calcula_valor_mochila(mochilas[i-1][j],V) >(V[i][1] + calcula_valor_mochila(mochilas[i-1][j-V[i][0]],V)): 
                    mochilas[i][j] = mochilas[i-1][j].copy()
                else:
                    mochilas[i][j] = mochilas[i-1][j-V[i][0]].copy()
                    mochilas[i][j] += [i]
    return (mochilas[n-1][K-1])

def gera_todas_mochilas(n):
    """gera todas as mochilas possiveis, dado um numero n de elementos disponíveis para serem colocados na mochila"""
    objetos = list(range(n))
    mochilas = list()
    for i in range(n+1):
        mochilas += list(combinations(objetos,i))
    #mochilas = [objetos[i:j] for i in range(n) for j in range(i+1,n+1)]
    return mochilas

def mochila_forca_bruta_iterativo(K,V):
    """Recebe uma capacidade K e um vetor de objetos V, e retorna a melhor mochila"""
    mochilas = gera_todas_mochilas(len(V))
    melhor_mochila = []
    for mochila in mochilas:
        if calcula_peso_mochila(mochila,V)<=K:
            if calcula_valor_mochila(mochila,V) > calcula_valor_mochila(melhor_mochila,V):
                melhor_mochila = mochila

    return melhor_mochila


def main():
    # os objetos sao formados por (PESO,VALOR), entao uma tupla (4,2) representa um objeto que pesa 4 e tem valor 2
    objetos = [(1,3),
               (2,4),
               (3,5),
               (5,1),
               (4,6),
               (3,2),
               (10,1),
               (1,10)]
    capacidade = 10


    print('-----------Mochila com PD---------')
    mochila = mochila_PD(capacidade,objetos)
    print(mochila)
    print(f'Valor = {calcula_valor_mochila(mochila,objetos)}')
    print(f'Peso = {calcula_peso_mochila(mochila,objetos)}')
    print('---------Mochila força bruta------')
    mochila = mochila_forca_bruta_iterativo(capacidade,objetos)
    print(mochila)
    print(f'Valor = {calcula_valor_mochila(mochila,objetos)}')
    print(f'Peso = {calcula_peso_mochila(mochila,objetos)}')
    
if __name__ == '__main__':
    main()
