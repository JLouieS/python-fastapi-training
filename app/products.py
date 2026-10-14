import json

def load_products(filename: str) -> list[dict]:
    """
    Load products from a JSON file.

    :param filename: The path to the JSON file containing product data.
    :return: A list of dictionaries, each representing a product.
    """

    try:
        with open(filename, 'r') as file:
            products = json.load(file)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: The file '{filename}' is not a valid JSON file.")
        return []    
    return products

def available_products(products: list[dict]) -> list[dict]:
    """
    Filter and return products that are available (in stock).

    :param products: A list of product dictionaries.
    :return: A list of available product dictionaries.
    """
    return [product for product in products if product.get('stock', False)]

def products_by_category(products: list[dict], category: str) -> list[dict]:
    """
    Filter and return products that belong to a specific category.

    :param products: A list of product dictionaries.
    :param category: The category to filter by.
    :return: A list of product dictionaries in the specified category.
    """
    return [product for product in products if product.get('category') == category]

def total_inventory_value(products: list[dict]) -> float:
    """
    Calculate the total inventory value of all products.

    :param products: A list of product dictionaries.
    :return: The total inventory value as a float.
    """
    return sum(product.get('price', 0) * product.get('stock', 0) for product in products)

def build_summary(products: list[dict]) -> dict:
    """
    Build a summary report of the products.

    :param products: A list of product dictionaries.
    :return: A dictionary containing the summary report.
    """
    summary = {
        "product_count": len(products),
        "available_product_count": len(available_products(products)),
        "out_of_stock_count": len([p for p in products if not p.get('stock', False)]),
        "inventory_value": total_inventory_value(products),
        "categories": sorted({p["category"] for p in products})
    }
    return summary

def save_report(report: dict, filename: str) -> None:
    """
    Save the summary report to a JSON file.

    :param report: The summary report as a dictionary.
    :param filename: The path to the JSON file where the report will be saved.
    """

    try:
        with open(filename, 'w') as file:
            json.dump(report, file, indent=4)
    except IOError:
        print(f"Error: Could not write to file '{filename}'.")

class ProductNotFoundError(Exception):
    pass


def find_product(products: list[dict], product_id: int) -> dict:
    """
    Find a product by its ID.

    :param products: A list of product dictionaries.
    :param product_id: The ID of the product to find.
    :return: The product dictionary if found.
    :raises ProductNotFoundError: If the product with the given ID is not found.
    """
    for product in products:
        if product.get('id') == product_id:
            return product
    raise ProductNotFoundError(f"Product with ID {product_id} not found.")
