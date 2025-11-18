def czy_parzysta(liczba: int) -> bool:
    return liczba % 2 == 0
wynik: bool = czy_parzysta(5)
if wynik:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")
