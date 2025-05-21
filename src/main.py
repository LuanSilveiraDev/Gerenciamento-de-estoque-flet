import flet as ft
import psycopg2
import re
from models.connection import DataBaseManager




def main(page: ft.Page):
    db = DataBaseManager()
    
    
    page.window.full_screen = False
    page.window.maximized = False
    page.window.resizable = False
        
    page.window.max_width = 1200
    page.window.max_height = 800
    
    content_area = ft.Column(
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True 
    )


    def adicionar_itens():
        desc_field = ft.TextField(label="Descrição do produto")
        mark_field = ft.TextField(label="Marca do produto")
        value_field = ft.TextField(label="Valor do produto", keyboard_type=ft.KeyboardType.NUMBER)
        stock_field = ft.TextField(label="Quantidade em estoque", keyboard_type=ft.KeyboardType.NUMBER)
        
        def add_item(e):
            description = desc_field.value.strip()
            mark = mark_field.value.strip()
            value = float(value_field.value)
            stock_quantity = int(stock_field.value)
        
            if not description or not mark:
                print("Alguma coisa")
                page.update()
            elif value < 0 or stock_quantity < 0 :
                print("Alguma coisa 2")
                page.update()
            else:
                db.add_product(description, mark, value, stock_quantity)
                atualizar_tabela()
            
            desc_field.value = ""
            mark_field.value = ""
            value_field.value = ""
            stock_field.value = ""
            page.update()
            
        
        btn_add_item = ft.ElevatedButton("Adicionar Item", on_click=add_item)
        return [
            desc_field,
            mark_field,
            value_field,
            stock_field,
            btn_add_item
        ]
    

    def adicionar_clientes():
        name_field = ft.TextField(label="Nome do Cliente")
        email_field = ft.TextField(label="Email do Cliente")
        
        def add_client(e):
            name = name_field.value.strip()
            email = email_field.value.strip()
            
            if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
                db.add_cliente(name,email)
            else:
                print("alguma coisa")
            
            name_field.value = ""
            email_field.value = ""
            page.update()
        
        btn_add_item = ft.ElevatedButton("Adicionar cliente", on_click=add_client)    
        return [
            name_field,
            email_field,
            btn_add_item
        ]
    
    
    def atualizar_tabela():
        content_area.controls = db.view_product()
        content_area.update()

    def handle_change(e):
        index = e.control.selected_index
        match index:
            
            case 0:
                atualizar_tabela()
                page.scroll = "always"
                page.update()
            case 1:
                content_area.controls = adicionar_itens()
            case 2:
                content_area.controls = adicionar_clientes()
        
                
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
            expand=True
        )
    )

ft.app(target=main)