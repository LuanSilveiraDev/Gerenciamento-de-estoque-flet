from repository.product_repository import ProductRepository
from models.product_model import Product
import flet as ft
from flet_toast import flet_toast

class ProductService:
    def __init__(self):
        self.repo = ProductRepository()
        
    def add_product(self, description, mark, value, stock_quantity, page: ft.Page):
        if not description or not mark:
            flet_toast.warning  (
                page=page,
                message="Descrição e marca são obrigatórios.",
                duration=5,
            )
            return 
        elif value <= 0 or stock_quantity <= 0 :
            flet_toast.warning(
                page=page,
                message="O valor e a quantidade em estoque não pode ser 0",
                duration=5
            )
            return
        product = Product(description=description, mark=mark, value=value, stock_quantity=stock_quantity)
        self.repo.add_product(product)
    
    def list_products(self):
        return self.repo.get_all()

    def delete_product(self, product_id):
        self.repo.delete(product_id)