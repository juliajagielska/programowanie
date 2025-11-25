class Property:
    def __init__(self, area: float, rooms: int, price: float, address: str) -> None:
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self) -> str:
        return (
            f"Nieruchomość:\n"
            f" powierzchnia: {self.area} m2\n"
            f" pokoje: {self.rooms}\n"
            f" cena: {self.price} zł\n"
            f" adres: {self.address}"
        )


class House(Property):
    def __init__(self, area: float, rooms: int, price: float, address: str, plot: int) -> None:
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self) -> str:
        base = super().__str__()
        return base + f"\n działka: {self.plot} m2"


class Flat(Property):
    def __init__(self, area: float, rooms: int, price: float, address: str, floor: int) -> None:
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self) -> str:
        base = super().__str__()
        return base + f"\n piętro: {self.floor}"


if __name__ == "__main__":
    house = House(
        area=120.0,
        rooms=5,
        price=950_000,
        address="Warszawa, ul. Zielona 1",
        plot=500,
    )

    flat = Flat(
        area=55.5,
        rooms=2,
        price=650_000,
        address="Kraków, ul. Słoneczna 10/5",
        floor=3,
    )


    print("Dom:")
    print(house)
    print()
    print("Mieszkanie:")
    print(flat)