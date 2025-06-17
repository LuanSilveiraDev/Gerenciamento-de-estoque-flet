import flet as ft
from services.client_service import ClientService
from models.client_model import Client
from repository.client_repository import ClientRepository

class ClientUI:
    def __init__(self, refresh_client):
        self.update = ClientRepository()
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
        
    def build_table_client(self):
        
        search_input = ft.TextField(
            label="Buscar cliente",
            hint_text="Digite o nome do Cliente",
            width=400
        )
        
        clients = self.service.list_client()
        
        
        table = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Nome")),
                ft.DataColumn(ft.Text("Email")),
                ft.DataColumn(ft.Text("Deletar"))
            ],
            rows=[]
        )
        
        
        def fill_table(query="") -> None:
            query = query.lower()
            filtered = [
                c for c in clients
                if query in c.name.lower()
                or query in c.email.lower()
            ] if query else clients
            
            table.rows.clear()
            
            for c in filtered:
                table.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(c.name)),
                            ft.DataCell(ft.Text(c.email)),
                            ft.DataCell(ft.IconButton("delete", icon_color="red", data=c.id, on_click=self.delete_client))
                        ]
                    )
                )
            
            if table.page:
                table.update()
        
        search_input.on_change = lambda e: (fill_table(e.control.value), table.update())
        
        fill_table()
        
        form_datable = ft.Container(
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
            
        return form_datable
        
    def delete_client(self,e):
        client_id = e.control.data
        self.service.delete_client(client_id)
        self.refresh_client()
    