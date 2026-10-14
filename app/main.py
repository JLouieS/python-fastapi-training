from services.product_loader import load_products
from services.product_service import ProductService, ProductNotFoundError

if __name__ == "__main__":
    service = ProductService(load_products("data/products.json"))
    print([p.name for p in service.get_available()])   # ['Keyboard', 'Monitor']
    print(service.find(3).name)                        # Monitor
    print(service.inventory_value())                   # 83000

    try:
        service.find(99)
    except ProductNotFoundError as e:
        print(f"Caught: {e}")
