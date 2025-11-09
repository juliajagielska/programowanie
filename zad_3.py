# Funkcja, która otrzymuje listę 5 liczb i zwraca listę,
# w której każda liczba jest pomnożona przez 2 (wersja z listą składaną)

def pomnoz_przez_dwa(lista_liczb):
    return [liczba * 2 for liczba in lista_liczb]

# Przykładowe wywołanie funkcji
liczby = [1, 2, 3, 4, 5]
wynik = pomnoz_przez_dwa(liczby)
print(wynik)