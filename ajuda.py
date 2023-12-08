import flet as ft
import sqlite3

casa=True

conexao=sqlite3.connect('dadosajuda.db', check_same_thread=False)
cursor=conexao.cursor()

def tabela_base():
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS clientes (
        id  INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT)'''
    )

class App(ft.UserControl):
    def __init__(self):
        super().__init__()
        #Construção dos controles
        self.todos_dados=ft.Column(auto_scroll=True)
        self.adicionar_dados=ft.TextField(label='Nome do dado')
        self.editar_dados=ft.TextField(label='Editar')
    
    def renderizar_todos(self):
        pass

    def adicionar_novo_dado(self, e):
        cursor.execute('INSERT INTO clientes (nome) VALUES (?)',
            [self.adicionar_dados.value])
        
        self.todos_dados.controls.clear()
        self.renderizar_todos()
        self.page.update()

    def build(self):
        return ft.Column([
            ft.Text('CRUD e SQLite'),
            self.adicionar_dados,
            ft.ElevatedButton('Adicionar dado',
                on_click=self.adicionar_novo_dado),
            self.todos_dados        
        ])
    
def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.title = "Cadastro"
    page.padding = 10
    page.window_width = 400
    page.window_height = 650
    page.theme_mode = ft.ThemeMode.DARK  

    minha_aplicacao=App()
    

    page.add(
        minha_aplicacao,     
    )
    

ft.app(target=main) if casa else ft.app(target=main, view=ft.AppView.WEB_BROWSER)