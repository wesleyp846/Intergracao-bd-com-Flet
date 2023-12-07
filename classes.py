import sqlite3
import flet as ft

class Contato:
    def __init__(self, nome, tel, email, endereco):
        self.nome=nome
        self.tel=tel
        self.email=email
        self.endereco=endereco

class Dados:
    def __init__(self, nome_banco):
        self.conexao = sqlite3.connect(nome_banco, check_same_thread=False)
        self.comando = self.conexao.cursor()

    def ler_dados(self):
        db=Dados('banco.db')
        db.comando.execute("SELECT * FROM contatos")
        return db.comando.fetchall()
    
    def salvar_dados(self, nome, tel, email, endereco):
        self.comando.execute("INSERT INTO contatos (nome, tel, email, endereco) VALUES (?, ?, ?, ?)", (nome, tel, email, endereco,))
        self.conexao.commit()

    def editar_dados(self, dado_antigo, dado_novo):
        db=Dados('banco.db')
        self.comando.execute("UPDATE contatos SET nome = ? WHERE nome = ?", (dado_novo,dado_antigo,))
        self.conexao.commit()
    
    def deletar_dados(self, dado):
        db=Dados('banco.db')
        self.comando.execute("DELETE FROM contatos WHERE nome = ?", (dado,))
        self.conexao.commit()

class Card:
    def __init__(self,nome):
        self.nome=nome
        
    def card_expansivel(nome='Nome', tel='Telefone', email='E-mail:', endereco='Endereço:'):
        cartao=Card(nome)
        db=Dados('banco.db')
        return ft.ExpansionTile(
            leading=ft.Icon(ft.icons.CONTACT_PHONE),
            title=ft.Text(nome),
            subtitle=ft.Text(tel),
            trailing=ft.Icon(ft.icons.ARROW_DROP_DOWN),
            controls=[
                ft.ListTile(
                    title=ft.Text(email),
                    subtitle=ft.Text(endereco),
                    trailing=ft.PopupMenuButton(
                        icon=ft.icons.MORE_VERT,
                        items=[
                            ft.PopupMenuItem(text="Editar",
                                on_click=lambda _: ft.Page.go("/incluir_contato"),
                            ),
                            ft.PopupMenuItem(text="Apagar",
                                on_click=lambda _: db.deletar_dados(cartao.nome),
                            ),
                        ]
                    )   
                )
            ]
        )
# Jorge=Contato("Jorge", "543322", "fdd@hhh", "")
# print(Jorge.endereco)
# Jorge.falar("eu to falando")