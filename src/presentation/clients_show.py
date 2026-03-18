import flet as ft
from services.client_service import ClientService
from repository.client_repository import ClientRepository
from repository.client_repository import Client
from presentation.clients_update import show_update_client

class ShowClient:
    def __init__(self, refresh_callback):
        self.update = ClientRepository()
        self.service  = ClientService()
        self.refresh_client = refresh_callback
        
        
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
                ft.DataColumn(ft.Text("Deletar")),
                ft.DataColumn(ft.Text("Atualizar"))
            ],
            rows=[]
        )
        
        def fill_table(query=""):
            query = query.lower()
            filtered = [
                c for c in clients
                if query in c.name.lower()
                or query in c.name.lower()
            ] if query else clients
            
            table.rows.clear()
            
            for c in filtered:
                table.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(c.name)),
                            ft.DataCell(ft.Text(c.name)),
                            ft.DataCell(ft.IconButton("delete", icon_color="red", data=c.id, on_click=self.delete_client)),
                            ft.DataCell(ft.IconButton("create", icon_color="blue",
                        data={
                            "id": c.id,
                            "name": c.name,
                            "email": c.email,
                        }, on_click=self.editar_cliente))
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

    def delete_client(self, e):
        client_id = e.control.data
        self.service.delete_client(client_id)
        self.refresh_client()
    
    def editar_cliente(self, e):
        data = e.control.data
        cliente = Client(
            id=data["id"],
            name=data["name"],
            email=data["email"]
        )
        
        def atualizar_callback(cliente_atualizado):
            self.update.update_client(cliente_atualizado)
            self.refresh_client()
        
        show_update_client(e.page, cliente, atualizar_callback)
    