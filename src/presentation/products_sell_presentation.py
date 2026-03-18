import flet as ft
from repository.client_products_sell import ClientProductsSell
from models.client_model import Client
from services.product_sell import ProductSell

class ProductClientSell:
    def __init__(self, update_client):
        self.repo = ClientProductsSell()
        self.service = ProductSell()
        self.update_client = update_client
        
    def load_data(self):
        clientes_dd = ft.Dropdown(label="Selecionar CLiente", width=300,  hint_text="Buscar...", enable_filter=True, editable=True)
        produtos_dd = ft.Dropdown(label="Buscar produto", width=300,hint_text="Buscar...", enable_filter=True, editable=True )
        cliente = self.service.clients_sell()
        produto = self.service.products_sell()
    
        clientes_dd.options = [ ft.dropdown.Option(str(c.id), c.name) for c in cliente]
        produtos_dd.options = [ft.dropdown.Option(str(p.id), p.mark, p.value) for p in produto]

        
        return [clientes_dd,
                produtos_dd]
        

           