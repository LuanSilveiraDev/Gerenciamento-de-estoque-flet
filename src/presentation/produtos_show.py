import flet as ft
from services.product_services import ProductService
from repository.product_repository import ProductRepository
from presentation.products_uptade_presentation import show_update_product
from models.product_model import Product

class ShowTable:
    def __init__(self, refresh_callback):
        self.update = ProductRepository()
        self.service = ProductService()
        self.refresh_callback = refresh_callback
        
    def build_table(self):

        search_input = ft.TextField(
            label="Buscar produto",
            hint_text="Digite nome, marca ou valor...",
            width=400
        )
        
        products = self.service.list_products()
        
        table = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Descrição")),
                ft.DataColumn(ft.Text("Marca")),
                ft.DataColumn(ft.Text("Valor")),
                ft.DataColumn(ft.Text("Quantidade")),
                ft.DataColumn(ft.Text("Deletar")),
                ft.DataColumn(ft.Text("Atualizar")),
            ],
            rows=[]
        )
        
        def fill_table(query="") -> None:
            query= query.lower()
            filtered = [
                p for p in products
                if query in p.description.lower()
                or query in p.mark.lower()
                or query in f"{p.value:.2f}"
            ] if query else products
            
            table.rows.clear()
            
            for p in filtered:
                table.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(f"{p.description}")),
                            ft.DataCell(ft.Text(p.mark)),
                            ft.DataCell(ft.Text(f"{p.value:.2f}")),
                            ft.DataCell(ft.Text(str(p.stock_quantity))),
                            ft.DataCell(ft.IconButton("delete", icon_color="red", data=p.id, on_click=self.delete_product)),
                            ft.DataCell(ft.IconButton("create", icon_color="blue",
                            data={
                                "id": p.id,
                                "description": p.description,
                                "mark": p.mark, 
                                "value": p.value,
                                "stock_quantity": p.stock_quantity
                            }, on_click=self.editar_produto))
                        ]
                    )
                )
            
            if table.page:
                table.update()
            
        search_input.on_change = lambda e: (fill_table(e.control.value), table.update())
        
        fill_table()
        
        form_datatable = ft.Container(
            content=ft.Column(
                controls=[
                    search_input,
                    table
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                scroll=ft.ScrollMode.ALWAYS,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            alignment=ft.alignment.center,
            padding=20
        )
        
        return form_datatable

    def delete_product(self, e):
        product_id = e.control.data
        self.service.delete_product(product_id)
        self.refresh_callback()
    
    def editar_produto(self, e):
        print("editar produto")
        data = e.control.data
        print("Controle do produto")
        produto = Product(
            id=data["id"],
            description=data["description"],
            mark=data["mark"],
            value=data["value"],
            stock_quantity=data["stock_quantity"]
            )
                
        def atualizar_callback(produto_atualizado):
            self.update.update_product(produto_atualizado)
            self.refresh_callback()
                
        show_update_product(e.page, produto, atualizar_callback)