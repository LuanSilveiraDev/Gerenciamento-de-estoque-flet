from repository.client_products_sell import ClientProductsSell

class ProductSell():
    def __init__(self):
        self.repo = ClientProductsSell()
    
    def clients_sell(self):
        return self.repo.load_clients_sell()
    
    def products_sell(self):
        return self.repo.load_products_sell()