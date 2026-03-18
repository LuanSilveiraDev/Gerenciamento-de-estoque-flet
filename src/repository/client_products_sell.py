from models.connection import DataBaseManager
from models.client_model import Client
from models.product_model import Product

class ClientProductsSell:
    def __init__(self):
        self.db = DataBaseManager()
        
    def load_clients_sell(self):
        self.db.cursor.execute(
            """
            SELECT id, name FROM cliente
            """
        )
        clientes = self.db.cursor.fetchall()
        
        return [Client(id=c[0], name=c[1]) for c in clientes]

    def load_products_sell(self):
        self.db.cursor.execute(
            """
            SELECT id, mark, value FROM produtos
            """
        )
        produtos = self.db.cursor.fetchall()
        
        return [Product(id=p[0], mark=p[1], value=p[2]) for p in produtos]
    
    def buy_products(self, client_id, product_id, quantity):
        self.db.cursor.execute(
            """
            INSERT INTO venda (client_id, product_id, quantity)
            VALUES (%s, %s, %s)
            """, (client_id, product_id, quantity)
        )
        self.db.conn.commit()       