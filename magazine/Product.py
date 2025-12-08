from dataclasses import dataclass

from magazine.utils import calculate_brutto


@dataclass
class Product:
    name: str
    net_price: float

    def brutto_price(self) -> float:
        return calculate_brutto(self.net_price)
