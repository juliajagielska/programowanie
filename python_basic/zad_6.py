from typing import List

def polacz_listy(lista1: List[int], lista2: List[int]) -> List[int]:

    polaczona = lista1 + lista2

    bez_duplikatow = set(polaczona)

    wynik = [x ** 3 for x in bez_duplikatow]

    return wynik

lista_a: List[int] = [1, 2, 3, 3]
lista_b: List[int] = [3, 4, 1]

rezultat: List[int] = polacz_listy(lista_a, lista_b)
print(rezultat)
