from models.connection import DataBaseManager
from models.product_model import Product

class ProductRepository:
    def __init__(self):
        self.db = DataBaseManager()
        
    def add_product(self, product: Product):
        self.db.cursor.execute(
            """
            INSERT INTO produtos (description, mark, value, stock_quantity)
            VALUES (%s, %s, %s, %s)
            """,(product.description, product.mark, product.value, product.stock_quantity)
        )
        self.db.conn.commit()
        
    def get_all(self):
        self.db.cursor.execute(
            """
            SELECT id, description, mark, value, stock_quantity FROM produtos
            """
        )
        result = self.db.cursor.fetchall()
        return [
            Product(id=r[0], description=r[1], mark=r[2], value=r[3], stock_quantity=r[4])
            for r in result
        ]
        
    def delete(self, product_id):
        self.db.cursor.execute("DELETE FROM produtos WHERE id = %s",(product_id,))
        self.db.conn.commit()
        
    def update_product(self, product: Product):
        self.db.cursor.execute(
            """
            UPDATE produtos
            SET description = %s,
                mark = %s,
                value = %s,
                stock_quantity = %s
            WHERE id = %s
            """,(product.description, product.mark, product.value, product.stock_quantity, product.id)
        )
        self.db.conn.commit()