# Funkcja, która otrzymuje listę 5 liczb i mnoży każdy element przez 2, zwraca wynik (wersja z pętlą for)

def pomnoz_przez_dwa(lista_liczb):
    nowa_lista = []
    for liczba in lista_liczb:
        nowa_lista.append(liczba * 2)
    return nowa_lista

# Przykładowe wywołanie funkcji
liczby = [1, 2, 3, 4, 5]
print(pomnoz_przez_dwa(liczby))