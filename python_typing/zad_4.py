def sprawdz_sume(a: int, b: int, c: int) -> bool:
    return a + b >= c


wynik: bool = sprawdz_sume(3, 5, 7)

if wynik:
    print("Suma dwóch pierwszych liczb jest większa lub równa trzeciej")
else:
    print("Suma dwóch pierwszych liczb jest mniejsza od trzeciej")
