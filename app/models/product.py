from dataclasses import dataclass


@dataclass
class Product:
    id: int
    name: str
    price: float
    stock: int
    category: str

    @property
    def is_available(self) -> bool:
        return self.stock > 0