from calculator import calculate_total


PRODUCTS = [
    {"name": "Mechanical Keyboard", "price": 3500.00, "quantity": 2, "discount": 10}
]


def print_order(product: dict) -> None:
    """
    Print the order details for a given product.

    :param product: A dictionary containing product details.
    """
    name = product.get("name")
    price = product.get("price")
    quantity = product.get("quantity")
    discount = product.get("discount", 0)

    total_price = calculate_total(price, quantity, discount)
    print(f"Product: {name}")
    print(f"Price: {price:.2f}")
    print(f"Quantity: {quantity}")
    print(f"Discount: {discount}%")
    print(f"Total: {total_price:.2f}")


def main() -> None:
    for product in PRODUCTS:
        print_order(product)


if __name__ == "__main__":
    main()
