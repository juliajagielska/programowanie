def calculate_brutto(net_price: float, vat_rate: float = 0.23) -> float:
    return net_price * (1 + vat_rate)
