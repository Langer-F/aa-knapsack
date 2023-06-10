from mochila_PD import mochila_PD,mochila_forca_bruta_iterativo,calcula_valor_mochila
from A_estrela import a_estrela
from memoizado import knapsack
from aproximacao import mochila_aproximado
import numpy as np

def gera_objetos_aleatorios(n,limite):
    objetos = []
    for _ in range(n):
        peso = np.random.randint(1,limite)
        valor = np.random.randint(1,limite)
        objetos += [(peso,valor)]
    return objetos

def main():
    objetos = [(1,1),
               (3,5),
               (4,2),
               (2,4),
               (6,9),
               (7,5),
               (1,10),
               (2,6),
               (8,5),
               (1,2),
               (10,3)]
    capacidade = 10
    print(f'Valores obtido com cada método para capacidade = {capacidade}:')
    print(f'Objetos = {objetos}')
    print(f'Força bruta iterativo: {calcula_valor_mochila(mochila_forca_bruta_iterativo(capacidade,objetos),objetos)}')
    print(f'Programacao Dinamica: {calcula_valor_mochila(mochila_PD(capacidade,objetos),objetos)}')
    print(f'A*: {calcula_valor_mochila(a_estrela(capacidade,objetos),objetos)}')
    mochila,valor = knapsack(objetos,capacidade)
    print(f'Memoizado: {valor}')

    print('-------------------------------------------------------')
    print('Agora testando com objetos aleatorios:')
    print('-------------------------------------------------------')
    numero_de_ciclos = 5
    objetos = gera_objetos_aleatorios(15,15)
    for _ in range(numero_de_ciclos):
        capacidade += 10
        print(f'Valores obtido com cada método para capacidade = {capacidade}:')
        print(f'Objetos = {objetos}')
        print(f'Força bruta iterativo: {calcula_valor_mochila(mochila_forca_bruta_iterativo(capacidade,objetos),objetos)}')
        print(f'Programacao Dinamica: {calcula_valor_mochila(mochila_PD(capacidade,objetos),objetos)}')
        print(f'A*: {calcula_valor_mochila(a_estrela(capacidade,objetos),objetos)}')
        mochila,valor = knapsack(objetos,capacidade)
        print(f'Memoizado: {valor}')
        print('--------------------------------------------')



if __name__ == '__main__':
    main()
