import flet as ft
from flet_toast import flet_toast
from models.client_model import Client
import re

def show_update_client(page: ft.Page, client: Client, on_update_callback):
    name_field = ft.TextField(label="Nome", value=client.name)
    email_field = ft.TextField(label="Email", value=client.email)
    
    def salvar(e):
        try:
            if not name_field.value:
                flet_toast.error(page=page, message="O nome do cliente é obrigatório", duration=5)
                return
            elif not email_field.value:
                flet_toast.error(page=page, message="O email tem que ser obrigatório", duration=5)
                return
            elif not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email_field.value):
                flet_toast.error(page=page, message="Email tem que está correto")
                return
            else:
                client.name = name_field.value
                client.email = email_field.value
                on_update_callback(client)
                dialog.open = False
                
                page.update()
                return True
        except exec as ex:
            print("Erro ao atualizar", ex)
            return False
    
    def on_click_salvar(e):
        if salvar(e):
            flet_toast.sucess(
                page=page,
                message="Cliente atualizado com sucesso!",
                duration=5
            )
        elif ValueError:
            flet_toast.error(
                page=page,
                message="Erro ao atualizar o cliente.",
                duration=5
            )
    
    def fechar(e):
        dialog.open = False
        page.update()
        
    dialog = ft.AlertDialog(
        title=ft.Text("Atualizar Cliente"),
        content=ft.Column(
            [
                name_field,
                email_field
            ], tight=True),
            actions=[
                ft.TextButton("Salvar", on_click=on_click_salvar),
                ft.TextButton("Cancelar", on_click=fechar)
            ],
            modal=True
    )
    
    if dialog not in page.controls:
        page.controls.append(dialog)
        
    page.dialog = dialog
    dialog.open = True
    page.update()