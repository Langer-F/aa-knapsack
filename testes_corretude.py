from mochila_PD import mochila_PD,mochila_forca_bruta_iterativo,calcula_valor_mochila
from A_estrela import a_estrela
from memoizado import knapsack



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

if __name__ == '__main__':
    main()
