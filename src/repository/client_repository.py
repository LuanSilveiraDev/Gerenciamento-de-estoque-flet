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
        
    def get_all(self):
        self.db.cursor.execute(
            """
            SELECT id, name, email FROM cliente
            """
        )
        result = self.db.cursor.fetchall()
        return [
            Client(id=r[0], name=r[1], email=r[2])
            for r in result
        ]
    
    def delete_client(self, client_id):
        self.db.cursor.execute(
            """
            DELETE FROM cliente WHERE id = %s
            """,(client_id,)
        )
        self.db.conn.commit()
        