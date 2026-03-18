from repository.client_repository import ClientRepository
from models.client_model import Client
import re

class ClientService():
    def __init__(self):
        self.repo = ClientRepository()
        
        
    def add_client(self, name, email):
        if not name or not email or not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            raise ValueError("E-mail inválido ou Campos faltando")
        client = Client(name=name, email=email)
        self.repo.add_cliente(client)

    
    def list_client(self):
        return self.repo.get_all()
    
    def delete_client(self, client_id):
        self.repo.delete_client(client_id)