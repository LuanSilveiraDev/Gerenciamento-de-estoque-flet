import psycopg2
import flet as ft
from dotenv import load_dotenv
import os
# conn = psycopg2.connect(database="Gerenciamento_estoque",
#                         host="localhost",
#                         user="luan",
#                         password="Refen123456",
#                         port="5432")

# cursor = conn.cursor()

load_dotenv()


class DataBaseManager:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
        self.cursor = self.conn.cursor()
        
    def add_product(self, description, mark, value, stock_quantity):
        self.cursor.execute(
            """
            INSERT INTO produtos (description, mark, value, stock_quantity)
            VALUES (%s, %s, %s, %s);
            """, (description, mark, value, stock_quantity)
        )
        self.conn.commit()

    def add_cliente(self, name, email):
        self.cursor.execute(
            """
            INSERT INTO cliente (name, email)
            VALUES (%s, %s);
            """, (name, email)
        )
        self.conn.commit()
    
    def view_product(self, refresh_callback):
        self.cursor.execute(
            """
            SELECT id,description, mark, value, stock_quantity FROM produtos;
            """
        )
        result = self.cursor.fetchall()
        columns = [column[0] for column in self.cursor.description]
        rows = [dict(zip(columns,row))for row in result]
        print(columns)
        print(rows)
        
        
        texto_estoque = ft.Text("Estoque de produtos")
        mydt = ft.DataTable(
              columns=[
                  ft.DataColumn(ft.Text("Descrição")),
                  ft.DataColumn(ft.Text("Marca")),
                  ft.DataColumn(ft.Text("Valor")),
                  ft.DataColumn(ft.Text("Quantidade")),
                  ft.DataColumn(ft.Text("Deletar"))
              ],
              rows=[]
        )
        
        mydt_cener = ft.Container(
            content=ft.Column(
                controls=[
                   texto_estoque,
                   mydt
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            alignment=ft.alignment.center,
            padding=20
        )
        
        
        for row in rows:
            mydt.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(row["description"])),
                        ft.DataCell(ft.Text(row["mark"])),
                        ft.DataCell(ft.Text(f'{row["value"]:.2f}')),
                        ft.DataCell(ft.Text(row["stock_quantity"])),
                        ft.DataCell(
                            ft.Row(
                                [ft.IconButton("delete", icon_color="red",
                                               data=row,
                                               on_click=lambda e, pid=row["id"]: deletebtn(e,pid))]
                                )),
                    ]
                )
            )
        
        def deletebtn(e, id):
            delete = "DELETE FROM produtos WHERE id = %s"
            self.cursor.execute(delete, (id,)) 
            self.conn.commit()
            refresh_callback()
            
            
        
        return [mydt_cener]

    
