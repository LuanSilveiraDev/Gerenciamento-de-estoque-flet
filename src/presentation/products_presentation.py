import flet as ft
from services.product_services import ProductService
from flet_toast import flet_toast

class ProductUI:
    def __init__(self, refresh_callback):
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
                    int(stock_field.value),
                    e.page
                )
                desc_field.value = mark_field.value = value_field.value = stock_field.value = ""
                self.refresh_callback()
            except Exception:
                flet_toast.error(
                    page=e.page,
                    message="Todos os campos devem ser preenchidos",
                    duration=5
                )
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
    
    
