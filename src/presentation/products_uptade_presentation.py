import flet as ft
from flet_toast import flet_toast
from models.product_model import Product

def show_update_dialog(page: ft.Page, product: Product, on_update_callback):
    print("Página recebida no diálogo:", page)
    desc_field = ft.TextField(label="Descrição", value=product.description)
    mark_field = ft.TextField(label="Marca", value=product.mark)
    value_field = ft.TextField(label="Valor", value=str(product.value)) 
    stock_field = ft.TextField(label="Estoque", value=str(product.stock_quantity))  
    
    def salvar(e):
        try:
            if not desc_field.value:
                flet_toast.error(page=page, message="O nome do produto é obrigatório.", duration=5)
                return
            elif not mark_field.value:
                flet_toast.error(page=page, message="A marca do produto é obrigatória.", duration=5)
                return
            elif not value_field.value:
                flet_toast.error(page=page, message="O valor do produto é obrigatório.", duration=5)
                return
            elif not stock_field.value:
                flet_toast.error(page=page, message="A quantidade em estoque é obrigatória.", duration=5)
                return
            elif not value_field.value.replace(',','.'):
                flet_toast.error(page=page, message="O valor deve ser um número.", duration=5)
                return
            else:
                product.description = desc_field.value
                product.mark = mark_field.value
                product.value = float(value_field.value)
                product.stock_quantity = int(stock_field.value)
                on_update_callback(product)
                dialog.open = False
                
                page.update()
                return True
        except Exception as ex:
            print("Erro ao atualizar", ex)
            return False
        
    def on_click_salvar(e):
        if salvar(e):
            flet_toast.sucess(
                page=page,
                message="Produto atualizado com sucesso!",
                duration=5
            )
        elif ValueError:
            flet_toast.error(
                page=page,
                message="Erro ao atualizar o produto.",
                duration=5
            )
    
    
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
            ft.TextButton("Salvar", on_click=on_click_salvar),
            ft.TextButton("Cancelar", on_click=fechar),
        ],
        modal=True
    )
    
    if dialog not in page.controls:
        page.controls.append(dialog)

    page.dialog = dialog
    dialog.open = True
    page.update()
