import pytest

from models.product import Product
from services.product_service import ProductService, ProductNotFoundError


@pytest.fixture
def products() -> list[Product]:
    return [
        Product(id=1, name="Keyboard", price=3500, stock=10, category="peripherals"),
        Product(id=2, name="Mouse", price=1500, stock=0, category="peripherals"),
        Product(id=3, name="Monitor", price=12000, stock=4, category="display"),
    ]


@pytest.fixture
def service(products) -> ProductService:
    return ProductService(products)


def test_find_returns_matching_product(service):
    result = service.find(1)

    assert result.name == "Keyboard"


def test_find_missing_product_raises(service):
    with pytest.raises(ProductNotFoundError):
        service.find(99)

def test_get_available_returns_only_available_products(service):
    result = service.get_available()

    assert [p.name for p in result] == ["Keyboard", "Monitor"]


def test_inventory_value(service):
    result = service.inventory_value()

    assert result == 83000

def test_empty_list_get_available_returns_empty():
    service = ProductService([])

    result = service.get_available()

    assert result == []

def test_empty_list_inventory_value_returns_zero():
    service = ProductService([])

    result = service.inventory_value()

    assert result == 0

def test_empty_list_find_raises():
    service = ProductService([])

    with pytest.raises(ProductNotFoundError):
        service.find(1)

def test_is_available_false_when_stock_zero():
    product = Product(id=1, name="Mouse", price=1500, stock=0, category="peripherals")

    assert not product.is_available