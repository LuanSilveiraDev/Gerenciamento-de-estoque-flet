import flet as ft
from models.product_model import Product

def show_update_dialog(page: ft.Page, product: Product, on_update_callback):
    print("Página recebida no diálogo:", page)
    desc_field = ft.TextField(label="Descrição", value=product.description)
    mark_field = ft.TextField(label="Marca", value=product.mark)
    value_field = ft.TextField(label="Valor", value=str(product.value)) 
    stock_field = ft.TextField(label="Estoque", value=str(product.stock_quantity))  
    
    def salvar(e):
        try:
            product.description = desc_field.value
            product.mark = mark_field.value
            product.value = float(value_field.value)
            product.stock_quantity = int(stock_field.value)
            on_update_callback(product)
            dialog.open = False
            page.update()
        except Exception as ex:
            print("Erro ao atualizar", ex)
            
    def fechar(e):
        dialog.open = False
        page.update()
    
    dialog = ft.AlertDialog(
        title=ft.Text("Atualizar Produto"),
        content=ft.Column([
            desc_field,
            mark_field,
            value_field,
            stock_field,
        ],tight=True),
        actions=[
            ft.TextButton("Salvar", on_click=salvar),
            ft.TextButton("Cancelar", on_click=fechar),
        ],
        modal=True
    )
    
    if dialog not in page.controls:
        page.controls.append(dialog)

    page.dialog = dialog
    dialog.open = True
    page.update()
