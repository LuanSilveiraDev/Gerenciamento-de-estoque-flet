from repository.product_repository import ProductRepository
from models.product_model import Product

class ProductService:
    def __init__(self):
        self.repo = ProductRepository()
        
    def add_product(self, description, mark, value, stock_quantity):
        if not description or not mark:
            raise ValueError("Campos obrigatórios")
        elif value <= 0 or stock_quantity <= 0 :
            raise ValueError("Valor ou quantidade inválidos")
        product = Product(description=description, mark=mark, value=value, stock_quantity=stock_quantity)
        self.repo.add_product(product)
    
    def list_products(self):
        return self.repo.get_all()

    def delete_product(self, product_id):
        self.repo.delete(product_id)