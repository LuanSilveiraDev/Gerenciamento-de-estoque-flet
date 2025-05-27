import flet as ft
from presentation.products_presentation import ProductUI
from presentation.clients_presentation import ClientUI

def main(page: ft.Page):
  
    page.window.resizable = False
    page.window.full_screen = False
    page.window.maximized = False
 
        
    page.window.max_width = 1000
    page.window.max_height = 800

    
    content_area = ft.Column(
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True 
    )

    def show_table():
        content_area.controls = [ProductUI(show_table).build_table()]
        content_area.update()

    def add_form():
        content_area.controls = ProductUI(show_table).build_form_product()
        content_area.update()
    
    
    def update_client():
        content_area.controls = [*ClientUI(update_client).buid_form_client()]
        content_area.update()
    
    def add_client():
        content_area.controls = ClientUI(update_client).buid_form_client()
        content_area.update()
    
    def handle_change(e):
        index = e.control.selected_index
        match index:
            
            case 0:
                show_table()
                page.scroll = "always"
                page.update()
            case 1:
                add_form()
            case 2:
                add_client()
        
                
        # if index == 0:
        #     atualizar_tabela()
        #     page.scroll = "always"
        #     page.update()
        # elif index == 1:
        #     content_area.controls = adicionar_itens()
        # elif index == 2:
        #     content_area.controls = [ft.Text("Voce clicou no item 3")]
            
        content_area.update()
        drawer.open = False
        drawer.update()
        print(f"Selected Index changed: {e.control.selected_index}")
 

 
    drawer = ft.NavigationDrawer(
        on_change=handle_change,
        controls=[
            ft.Container(height=12),
            ft.NavigationDrawerDestination(
                label="Estoque",
                icon=ft.Icons.DOOR_BACK_DOOR_OUTLINED,
                selected_icon=ft.Icon(ft.Icons.DOOR_BACK_DOOR),
            ),
            ft.Divider(thickness=2),
            ft.NavigationDrawerDestination(
                icon=ft.Icon(ft.Icons.MAIL_OUTLINED),
                label="Adicionar item",
                selected_icon=ft.Icons.MAIL,
            ),
            ft.NavigationDrawerDestination(
                icon=ft.Icon(ft.Icons.PHONE_OUTLINED),
                label="Produtos Vendidos",
                selected_icon=ft.Icons.PHONE,
            ),
        ],  
    )
    
    
    show_drawer_button = (ft.ElevatedButton("Gerenciamento de Estoque", 
                                            icon=ft.Icons.WAVES_ROUNDED, 
                                            width=300,
                                            height=50, 
                                            offset = ft.Offset(0,0),
                                            on_click=lambda e: page.open(drawer),
                                            ))


    page.add(
        ft.Column(
            controls=[
                show_drawer_button,
                content_area,
                ],
            expand=True,
        )
    )
    
    show_table()

ft.app(target=main)