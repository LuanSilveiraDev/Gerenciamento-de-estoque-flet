from models.connection import DataBaseManager
from models.client_model import Client

class ClientRepository:
    def __init__(self):
        self.db = DataBaseManager()
    
    def add_cliente(self, client: Client):
        self.db.cursor.execute(
            """
            INSERT INTO cliente (name, email)
            VALUES (%s, %s);
            """, (client.name, client.email)
        )
        self.db.conn.commit()