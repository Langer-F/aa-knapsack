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

def pode_colocar_algo_na_mochila(mochila,objetos,capacidade):
    """Verifica se ainda é possivel colocar alguma coisa na mochila"""
    peso_atual = calcula_peso_mochila(mochila,objetos)
    for i in range(len(objetos)):
        if i not in mochila:
            if peso_atual + objetos[i][0] <=capacidade:
                return True
    return False

def calcula_heuristica(Mochila,Objetos,Capacidade):
    peso_total_que_nao_esta_na_mochila = 0
    valor_total_que_nao_esta_na_mochila = 0

    for i in range(len(Objetos)):
        if i not in Mochila:
            peso_total_que_nao_esta_na_mochila += Objetos[i][0]
            valor_total_que_nao_esta_na_mochila += Objetos[i][1]

    densidade_geral = valor_total_que_nao_esta_na_mochila/peso_total_que_nao_esta_na_mochila
    peso_restante = Capacidade - calcula_peso_mochila(Mochila,Objetos)
    return densidade_geral*peso_restante

def a_estrela(Capacidade,Objetos):
    if Capacidade ==0:
        return []
    mochila = []
    while pode_colocar_algo_na_mochila(mochila,Objetos,Capacidade):
        maior_valor = 0
        maior_i = -1
        for i in range(len(Objetos)):
            if i not in mochila and ((calcula_peso_mochila(mochila,Objetos)+Objetos[i][0])<=Capacidade):
                mochila_temporaria = mochila.copy()
                mochila_temporaria += [i]
                valor = calcula_valor_mochila(mochila_temporaria,Objetos) + calcula_heuristica(mochila_temporaria,Objetos,Capacidade)
                if valor>maior_valor:
                    maior_valor = valor
                    maior_i = i
        
        if maior_i not in mochila:
            mochila += [maior_i]
    return mochila

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
    objetos = [(1,3),
               (2,4),
               (3,5),
               (5,1),
               (4,6),
               (3,2),
               (10,1),
               (1,10)]
    capacidade = 10
    
    print('-----------Mochila com A*---------')
    mochila = a_estrela(capacidade,objetos)
    print(mochila)
    print(f'Valor = {calcula_valor_mochila(mochila,objetos)}')
    print(f'Peso = {calcula_peso_mochila(mochila,objetos)}')
    print('---------Mochila força bruta------')
    mochila = mochila_forca_bruta_iterativo(capacidade,objetos)
    print(mochila)
    print(f'Valor = {calcula_valor_mochila(mochila,objetos)}')
    print(f'Peso = {calcula_peso_mochila(mochila,objetos)}')
    """
    mochila = [3]
    print(calcula_heuristica(mochila,objetos,capacidade))
    """

if __name__ == '__main__':
    main()