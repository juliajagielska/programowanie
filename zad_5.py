# Funkcja, która otrzymuje listę 10 liczb i wyświetla co drugi element

def co_drugi_element(lista_liczb):
    for i in range(0, len(lista_liczb), 2):
        print(lista_liczb[i])

# Przykładowe wywołanie funkcji
liczby = list(range(1, 11))
co_drugi_element(liczby)