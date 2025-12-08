from magazine.Order import Order
from magazine.Product import Product


def main() -> None:
    product1 = Product(name="Książka", net_price=50.0)
    product2 = Product(name="Długopis", net_price=5.0)

    order = Order(products=[product1, product2])

    print("Suma netto:", order.total_net())
    print("Suma brutto:", order.total_brutto())


if __name__ == "__main__":
    main()
