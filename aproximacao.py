from mochila_PD import mochila_PD, calcula_valor_mochila, calcula_peso_mochila, mochila_forca_bruta_iterativo
from math import floor

def mochila_aproximado(peso_maximo, vetor_tupla_peso_valor, erro=0.1):
    assert erro > 0 and erro < 1
    max_valor = -1
    for tupla_peso_valor in vetor_tupla_peso_valor:
        _, valor = tupla_peso_valor
        max_valor = max(max_valor, valor)

    lambda_divisor = erro * max_valor / len(vetor_tupla_peso_valor)

    vetor_tupla_peso_valor_atualizado = list(vetor_tupla_peso_valor)
    for i, tupla_peso_valor in enumerate(vetor_tupla_peso_valor_atualizado):
        peso, valor = tupla_peso_valor[0], floor(tupla_peso_valor[1] / lambda_divisor)
        vetor_tupla_peso_valor_atualizado[i] = (peso, valor)

    return mochila_PD(peso_maximo, vetor_tupla_peso_valor_atualizado)

def main():
    # os objetos sao formados por (PESO,VALOR), entao uma tupla (4,2) representa um objeto que pesa 4 e tem valor 2
    objetos = [(1,3),
               (2,4),
               (3,6),
               (5,2),
               (4,8),
               (20,2),
               (2,20),
               (10,10),
               (12,11),
               (3,4),
               (4,4),
               (5,6),
               (5,5),
               (3,3),
               (2,10),
               (30,19),
               (1,2),
               (4,1),
               (50,49),
               (5,6),
               (4,5),
               (10,2),
               (2,3),
               (5,4),
               (5,6),
               (4,6),
               (4,6),
               (3,13),
               (4,8),
               (5,9),
               (3,7),
               (1,11)]
    capacidade = 100


    print('-----------Mochila com Aprox---------')
    mochila = mochila_aproximado(capacidade,objetos,0.5)
    print(mochila)
    print(f'Valor = {calcula_valor_mochila(mochila,objetos)}')
    print(f'Peso = {calcula_peso_mochila(mochila,objetos)}')

    print('-----------Mochila com PD---------')
    mochila = mochila_PD(capacidade,objetos)
    print(mochila)
    print(f'Valor = {calcula_valor_mochila(mochila,objetos)}')
    print(f'Peso = {calcula_peso_mochila(mochila,objetos)}')

if __name__ == '__main__':
    main()
