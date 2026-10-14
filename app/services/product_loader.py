import json

from models.product import Product

def load_products(filename: str) -> list[Product]:
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
    return [Product(**product) for product in products]