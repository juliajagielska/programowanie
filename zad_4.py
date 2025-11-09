# Funkcja, która otrzymuje listę 10 liczb i wyświetla jedynie parzyste elementy

def pokaz_parzyste(lista_liczb):
    for liczba in lista_liczb:
        if liczba % 2 == 0:
            print(liczba)

# Przykładowe wywołanie funkcji
liczby = list(range(1, 11))
pokaz_parzyste(liczby)