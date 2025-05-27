import flet as ft
from services.client_service import ClientService


class ClientUI:
    def __init__(self, refresh_client):
        self.service = ClientService()
        self.refresh_client = refresh_client
        
    def buid_form_client(self):
        name_field = ft.TextField(label="Nome do cliente", width=500)
        email_field = ft.TextField(label="email do cliente", width=500)
        
        def submit(e):
            self.service.add_client(
                name_field.value.strip(),
                email_field.value.strip()
            )
            name_field.value = ""
            email_field.value = ""
            self.refresh_client()
            

            
    
    
        
        form_container = ft.Container(
            content=ft.Column(
                controls=[
                    name_field,
                    email_field
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            alignment=ft.alignment.center,
            padding=20
    )
        
        buttom = ft.ElevatedButton("Adicionar", on_click=submit)
        
        return [form_container,
                buttom]
        
        