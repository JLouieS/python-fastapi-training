
from models.product import Product

class ProductNotFoundError(Exception):
    pass

class ProductService:
    def __init__(self, products: list[Product]) -> None:
        self.products = products

    def get_available(self) -> list[Product]:
        return [product for product in self.products if product.is_available]

    def find(self, product_id: int) -> Product:
        for product in self.products:
            if product.id == product_id:
                return product
        raise ProductNotFoundError(f"Product with ID {product_id} not found.")

    def inventory_value(self) -> float:
        return sum(product.price * product.stock for product in self.products)

