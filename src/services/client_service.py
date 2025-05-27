from repository.client_repository import ClientRepository
from repository.client_repository import Client


class ClientService():
    def __init__(self):
        self.repo = ClientRepository()
        
        
    def add_client(self, name, email):
        if not name or not email:
            raise ValueError("Campos obrigadórios")
        else:
            client = Client(name=name, email=email)
            self.repo.add_cliente(client)
            
 