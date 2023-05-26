import unittest
import random

VALOR = 0
PESO = 1

def knapsack_recursivo(objetos: list, mochila_capacidade: int):
    if len(objetos) == 0 or mochila_capacidade <= 0:
        return ([], 0)
    resto_solucao_sem_lista, resto_solucao_sem_valor = knapsack_recursivo(objetos[1:], mochila_capacidade)

    objeto_a_pegar = objetos[0]
    resto_solucao_com_lista, resto_solucao_com_valor = [], 0
    if objeto_a_pegar[PESO] <= mochila_capacidade:
        resto_solucao_com_resto_lista, resto_solucao_com_resto_valor = knapsack_recursivo(objetos[1:], mochila_capacidade - objeto_a_pegar[PESO])
        resto_solucao_com_lista = [objeto_a_pegar] + resto_solucao_com_resto_lista
        resto_solucao_com_valor = objeto_a_pegar[VALOR] + resto_solucao_com_resto_valor

    if resto_solucao_com_valor > resto_solucao_sem_valor:
        return resto_solucao_com_lista, resto_solucao_com_valor
    return resto_solucao_sem_lista, resto_solucao_sem_valor

class KnapsackRecursivoTest(unittest.TestCase):
    def test_vazio(self):
        self.assertEqual(knapsack_recursivo([], 600)[0], [])
        self.assertEqual(knapsack_recursivo([], 200)[1], 0)

        self.assertEqual(knapsack_recursivo([(1,2), (3,4)], 0)[0], [])
        self.assertEqual(knapsack_recursivo([(5,3), (6,9)], 0)[1], 0)

    def test_escolhe_mais_menores_valendo_mais(self):
        CASO_CLASSICO = [(4000, 50),
                         (1000, 10),
                         (1000, 10),
                         (1000, 10),
                         (1000, 10),
                         (500, 10)
                         ]
        escolhas, valor_escolhas = knapsack_recursivo(CASO_CLASSICO, 50)
        self.assertEqual(valor_escolhas, 4500)

    def test_escolhe_os_mais_valiosos(self):
        CASO_CLASSICO = [(4000, 10),
                         (1000, 10),
                         (1000, 10),
                         (1000, 10),
                         (1000, 10),
                         (500, 10)
                         ]
        escolhas, valor_escolhas = knapsack_recursivo(CASO_CLASSICO, 50)
        self.assertEqual(valor_escolhas, 8000)

    def test_escolhe_os_mais_leves(self):
        CASO_CLASSICO = [(4000, 10),
                         (1000, 1),
                         (1000, 1),
                         (1000, 1),
                         (1000, 1),
                         (1000, 1),
                         (1000, 1),
                         (1000, 1),
                         (1000, 1),
                         (1000, 1),
                         (500, 5)
                         ]
        escolhas, valor_escolhas = knapsack_recursivo(CASO_CLASSICO, 10)
        self.assertEqual(valor_escolhas, 9000)

    def test_escolhe_mais_leve_mais_valioso(self):
        CASO_CLASSICO = [(40000, 10),
                         (1000, 1),
                         (1000, 1),
                         (1000, 1),
                         (1000, 1),
                         (1000, 1),
                         (1000, 1),
                         (1000, 1),
                         (1000, 1),
                         (1000, 1),
                         (500, 5)
                         ]
        escolhas, valor_escolhas = knapsack_recursivo(CASO_CLASSICO, 10)
        self.assertEqual(valor_escolhas, 40000)

    def test_nao_leva_boletos(self):
        CASO_CLASSICO = [(-40000, 10),
                         (-1000, 1),
                         (-1000, 1),
                         (-1000, 1),
                         (-1000, 1),
                         (-1000, 1),
                         (-1000, 1),
                         (-1000, 1),
                         (-1000, 1),
                         (-1000, 1),
                         (-500, 5)
                         ]
        escolhas, valor_escolhas = knapsack_recursivo(CASO_CLASSICO, 10)
        self.assertEqual(valor_escolhas, 0)

    def test_longo(self):
        itens = [(10,1), (100, 15), (5, 5), (15,2), (35,7), (30, 3), (3, 30), (7,10)]
        CASO_CLASSICO = []
        for i in range(30):
            CASO_CLASSICO += random.choices(itens)
        escolhas, valor_escolhas = knapsack_recursivo(CASO_CLASSICO, 60)
        self.assertNotEqual(len(escolhas), 0)

    def test_limite(self):
        itens = [(10,1), (100, 15), (5, 5), (15,2), (35,7), (30, 3), (3, 30), (7,10)]
        CASO_CLASSICO = []
        for i in range(31):
            CASO_CLASSICO += random.choices(itens)
        escolhas, valor_escolhas = knapsack_recursivo(CASO_CLASSICO, 60)
        self.assertNotEqual(len(escolhas), 0)

if __name__ == "__main__":
    unittest.main()
