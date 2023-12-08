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
    
    def deletar(self, x, y):
        cursor.execute('DELETE FROM clientes WHERE id = ?', [x])
        y.open=False

        #chamando a funçao render de renderizar dados
        self.todos_dados.controls.clear()
        self.renderizar_todos()
        self.page.update()
    
    def atualizar(self, x , y, z):
        cursor.execute('UPDATE clientes SET nome = ? WHERE id = ?', (y, x))
        conexao.commit()

        z.open=False

        #chamando a funçao render de renderizar dados
        self.todos_dados.controls.clear()
        self.renderizar_todos()
        self.page.update()

    '''def abrir_acoes(self, e):
        #criando a função para abrir as acoes
        id_user=e.controls.subtitle.value
        self.editar_dados.value = e.controls.title.value
        self.update()

        alerta_dialogo = ft.AlertDialog(
            title=ft.Text(f'Editar ID {id_user}'),
            content=self.editar_dados,

            #botoes de acao
            actions=[
                ft.ElevatedButton(
                    "Deletar",
                    color=ft.colors.WHITE,
                    bgcolor=ft.colors.RED,
                    on_click= lambda e: self.deletar(id_user, alerta_dialogo)
                ),
                ft.ElevatedButton(
                    'Atualizar',
                    on_click=lambda e: self.atualizar(id_user, self.editar_dado.value, alerta_dialogo)
                )
            ],
            actions_alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )

        self.page.dialog = alerta_dialogo
        alerta_dialogo.open=True

        #para atualizar a pagina
        self.page.update()
        '''
    
    def renderizar_todos(self):
    #Mostrar todos os dados do banco de dados
        cursor.execute('SELECT * FROM clientes')
        conexao.commit()
        print('foi chamada renderizar_todos')

        meus_dados = cursor.fetchall()

        for dado in meus_dados:
            #utilizo sempre o controls quando utilizo a super class Usercontrols
            
            self.todos_dados.controls.append(
                ft.ListTile(
                    title=ft.Text(dado[1]),
                    subtitle=ft.Text(dado[0]),
                    #on_click=self.abrir_acoes
                )
            )
        #self.update()

    def ciclo(self):
        #nao deixa o banco feochar a conecxao
        self.renderizar_todos()
        #self.update()

    def adicionar_novo_dado(self, e):
        cursor.execute('INSERT INTO clientes (nome) VALUES (?)',
            [self.adicionar_dados.value])
        conexao.commit()
        
        self.todos_dados.controls.clear()
        self.renderizar_todos()
        self.page.update()

    def build(self):
        self.ciclo()
        return ft.Column([
            ft.Text('CRUD e SQLite'),
            self.adicionar_dados,
            ft.ElevatedButton('Adicionar dado',
                on_click=self.adicionar_novo_dado),
            self.todos_dados,     
        ])

def main(page: ft.Page):
    page.update()
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.title = "Cadastro"
    page.padding = 10
    page.window_width = 400
    page.window_height = 650
    page.theme_mode = ft.ThemeMode.DARK

    tabela_base()
    minha_aplicacao=App()

    page.add(
        minha_aplicacao,     
    )
    

ft.app(target=main) if casa else ft.app(target=main, view=ft.AppView.WEB_BROWSER)