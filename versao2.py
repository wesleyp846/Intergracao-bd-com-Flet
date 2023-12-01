import flet as ft
import sqlite3

class DbModel:
    def __init__(self):
        self.conn = sqlite3.connect('dados.db', check_same_thread=False)
        self.create_table()
        
    def create_table(self):
        c = self.conn.cursor()
        c.execute(
            """
            CREATE TABLE IF NOT EXISTS clients (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                name TEXT
            )
            """
        )
        
    #def add(self, name):
    def add(self, e):
        c = self.conn.cursor()
        c.execute('INSERT INTO clients (name) VALUES (?)', 
        [e]),
        # c.execute(
        #     "INSERT INTO clients (name) VALUES (:name)",
        #     {"name": name} 
        # )
        self.conn.commit()
        c.close()
        
    # outras operações BD 

class App(ft.UserControl):

    def __init__(self):
        super().__init__()
        self.model = DbModel()
        self.input_name = ft.TextField(label='Nome do Cliente')#, on_submit=self.add_client)
        self.button_add = ft.ElevatedButton('Adicionar Cliente', on_click=self.add_client)
        #self.listview_clients = None #Na função bild tem que descomentar
        # inicialização interface
        
    def render_clients(self):
        clients = self.model.get_all() 
        # lógica renderizar na tela
        
    def add_client(self, name):  
        self.model.add(name)
        self.render_clients()
        
    def build(self):
        
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("Clientes"),  
                    self.input_name,
                    self.button_add,
                    #Falta implementar a lista de clientes
                    #self.listview_clients,
                ]
            )
        )

def main(page: ft.Page):
    page.window_width = 400
    page.window_height = 650
    app = App()
    page.add(app)
    #page.update()

ft.app(target=main)