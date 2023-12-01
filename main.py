import flet as ft
import sqlite3

# conectando ao banco de dados
conexao = sqlite3.connect('dados.db', check_same_thread=False)
cursor = conexao.cursor()

# criar tabela no bd


def tabela_base():
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, none TEXT)
        '''
    )


class App(ft.UserControl):

    def __init__(self):
        super().__init__()
        self.todos_dados = ft.Column(auto_scroll=True)
        self.adicionar_dados = ft.TextField(label='Nome do dado')
        self.editar_dado = ft.TextField(label='Editar')

    # função de deletar dado
    def deletar(self, x, y):
        cursor.execute('DELITE FROM clientes WHERE id = ?', [x])
        y.open = False

        # chamar a função de renderizar dados
        self.todos_dados.controls.clear()
        self.renderizar_todos()
        self.page.update()

    def atualizar(self, x, y, z):
        cursor.execute('UPDATE clientes SET NOME = ? WHERE id = ?', (y, x))
        conexao.commit()

        z.open = False

        self.todos_dados.controls.clear()
        self.adicionar_dados()
        self.page.update()

    # criando a função para abrir as ações
    def abrir_acoes(self, e):
        id_user = e.control.subtitle.value
        self.editar_dado.value = e.control.title.value
        self.update()

        alerta_dialogo = ft.AlertDialog(ft.Text(f'Editar ID {id_user}'),
                                        content=self.editar_dado,
                                        actions=[(
                                            ft.ElevatedButton(
                                                text='Deletar',
                                                color=ft.colors.AMBER,
                                                bgcolor='red',
                                                on_click=lambda e: self.deletar(
                                                    id_user, alerta_dialogo)
                                            ),
                                            ft.ElevatedButton(
                                                text='Atualizar',
                                                color=ft.colors.AMBER,
                                                on_click=lambda e: self.atualizar(
                                                    id_user, self.editar_dado.value, alerta_dialogo)
                                            ))
        ],
        )  # actions_alignment='spaceBetween')
        self.page.dialog = alerta_dialogo
        alerta_dialogo.open = True

        # atualizar a pagina
        self.update()

    # Mostrar dados do banco de dados
    def renderizar_todos(self):
        cursor.execute('SELECT * FROM clientes')
        conexao.commit()

        meus_dados = cursor.fetchall()

        for dado in meus_dados:
            self.todos_dados.controls.append(
                ft.ListTile(
                    subtitle=ft.Text(dado[0]),
                    title=ft.Text(dado[1]),
                    on_click=self.abrir_acoes
                )
            )
        self.update()

    def ciclo(self):
        self.renderizar_todos()

    # criar um dado dentro do banco de dados
    def adicionar_novo_dado(self, e):
        cursor.execute('INSERT INTO clientes (none) VALUES (?)', 
        [self.adicionar_dados.value]),
        conexao.commit()

        self.todos_dados.controls.clear()
        self.renderizar_todos()
        self.update()

    def build(self):
        return ft.Column(
            [
                ft.Container(
                    content=ft.Text("CRUD com SQLITE"),
                    alignment=ft.alignment.center,
                    margin=10,
                    padding=10,
                    border_radius=10,
                ),
                self.adicionar_dados,
                    ft.ElevatedButton('Adicionar dado',
                    on_click=self.adicionar_novo_dado),
                self.todos_dados
            ]
        )


def main(page: ft.Page):
    tabela_base()
    page.window_width = 400
    page.window_height = 650
    minha_aplicacao = App()
    page.add(minha_aplicacao)
    page.update()


ft.app(target=main)
