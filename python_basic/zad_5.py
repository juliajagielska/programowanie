from typing import List

def czy_na_liscie(lista: List[int], liczba: int) -> bool:
    return liczba in lista

moja_lista: List[int] = [1, 3, 5, 7, 9]
szukana_liczba: int = 5

wynik: bool = czy_na_liscie(moja_lista, szukana_liczba)

print(wynik)
