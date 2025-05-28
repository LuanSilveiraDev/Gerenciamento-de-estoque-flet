import flet as ft
from services.product_services import ProductService
from presentation.products_uptade_presentation import show_update_dialog
from models.product_model import Product
from repository.product_repository import ProductRepository

class ProductUI:
    def __init__(self, refresh_callback):
        self.update = ProductRepository()
        self.service = ProductService()
        self.refresh_callback = refresh_callback
        
        
    def build_form_product(self):
        text_stock = ft.Text("Estoque de produtos")
        desc_field = ft.TextField(label="Descrição do produto", width=500)
        mark_field = ft.TextField(label="Marca do produto", width=500)
        value_field = ft.TextField(label="Valor do produto", keyboard_type=ft.KeyboardType.NUMBER, width=500)
        stock_field = ft.TextField(label="Quantidade em estoque", keyboard_type=ft.KeyboardType.NUMBER, width=500)

        def submit(e):
            try:
                self.service.add_product(
                    desc_field.value.strip(),
                    mark_field.value.strip(),
                    float(value_field.value),
                    int(stock_field.value)
                )
                desc_field.value = mark_field.value = value_field.value = stock_field.value = ""
                self.refresh_callback()
            except Exception as ex:
                print("Erro:", ex)
            e.page.update()

                 
        form_container = ft.Container(
            content=ft.Column(
                controls=[
                    text_stock,
                    desc_field,
                    mark_field,
                    value_field,
                    stock_field
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            alignment=ft.alignment.center,
            padding=20
    )
        
        buttom = ft.ElevatedButton("Adicionar", on_click=submit)

        return [
            form_container,
            buttom
        ]    
    
    
    def build_table(self):
        products = self.service.list_products()
        table = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Descrição")),
                ft.DataColumn(ft.Text("Marca")),
                ft.DataColumn(ft.Text("Valor")),
                ft.DataColumn(ft.Text("Quantidade")),
                ft.DataColumn(ft.Text("Deletar")),
                ft.DataColumn(ft.Text("Atualizar"))
            ],
            rows=[]
        )
        
        
        for p in products:
            table.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(p.description)),
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
                            }, on_click=self.editar_produto)),
                    ]
                )
            )
            
            
        form_datatable = ft.Container(
            content=ft.Column(
                controls=[
                    table
                ],
                alignment=ft.MainAxisAlignment.CENTER,
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
        
        show_update_dialog(e.page, produto, atualizar_callback)