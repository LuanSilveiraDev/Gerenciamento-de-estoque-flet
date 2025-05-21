import psycopg2
import flet as ft
from dotenv import load_dotenv
import os


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
    
    def view_product(self):
        self.cursor.execute(
            """
            SELECT description, mark, value, stock_quantity FROM produtos;
            """
        )
        result = self.cursor.fetchall()
        columns = [column[0] for column in self.cursor.description]
        rows = [dict(zip(columns,row))for row in result]
        print(columns)
        print(rows)
        
        mydt = ft.DataTable(
              columns=[
                  ft.DataColumn(ft.Text("description")),
                  ft.DataColumn(ft.Text("mark")),
                  ft.DataColumn(ft.Text("value")),
                  ft.DataColumn(ft.Text("stock_quantity"))
              ],
              rows=[]
        )
        
        for row in rows:
            mydt.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(row["description"])),
                        ft.DataCell(ft.Text(row["mark"])),
                        ft.DataCell(ft.Text(f'{row["value"]:.2f}')),
                        ft.DataCell(ft.Text(row["stock_quantity"])),
                    ]
                )
            )
        return [mydt]


database = DataBaseManager()
print(database)
database.view_product()
