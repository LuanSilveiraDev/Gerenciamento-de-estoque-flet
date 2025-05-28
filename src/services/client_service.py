from repository.client_repository import ClientRepository
from repository.client_repository import Client
import re

class ClientService():
    def __init__(self):
        self.repo = ClientRepository()
        
        
    def add_client(self, name, email):
        if not name or not email or not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            raise ValueError("E-mail inválido ou Campos faltando")
        client = Client(name=name, email=email)
        self.repo.add_cliente(client)

            
 