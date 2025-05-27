from dataclasses import dataclass

@dataclass
class Product:
    id: int = None
    description: str = ""
    mark: str = ""
    value: float = 0.0
    stock_quantity: int = 0