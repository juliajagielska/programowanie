from dataclasses import dataclass
from typing import List

from magazine.Product import Product
from magazine.utils import calculate_brutto


@dataclass
class Order:
    products: List[Product]

    def total_net(self) -> float:
        return sum(product.net_price for product in self.products)

    def total_brutto(self) -> float:
        return calculate_brutto(self.total_net())
