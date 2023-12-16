import sqlite3
import flet as ft
from flet import *

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
    def __init__(self, nome):
        self.nome = nome

    def card_expansivel(nome='Nome', tel='Telefone', email='E-mail:', endereco='Endereço:'):
        cartao = Card(nome)
        db = Dados('banco.db')

        def editar_contato(e):
            tb1 = ft.TextField(label=cartao.nome)
            db = Dados('banco.db')
            db.editar_dados(cartao.nome,tb1.value)
            
            # Lógica para edição do contato
            print(f"Editar contato: {cartao.nome}")
            
            inputcon = Card(
                offset=transform.Offset(2,0),
                animate_offset=animation.Animation(600,curve='easyIn'),
                elevation=30,
                content=Container(
                    bgcolor='green200',
                    content=Column([
                        Row([
                            Text(f'Editar {cartao.nome}',size=20,weight='bold'),
                            IconButton(icon='close',icon_size=30), #on_click=hidecon),
                        ]),
                        # name,
                        # age, 
                        # contact,
                        # gender, 
                        # email, 
                        # address,
                        # FilledButton('Salvar dados', on_click=savedata)
                    ])
                )
            )
           

        def apagar_contato(e):
            try:
                # Lógica para apagar o contato
                db.deletar_dados(cartao.nome)
                print(f"Contato {cartao.nome} apagado com sucesso!")

                # Atualizar a página ou tomar outra ação necessária após apagar o contato
                # page.go("/mostar_contatos")  # Isso redirecionaria para a página de mostrar contatos
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
                                    ft.PopupMenuItem(
                                        text="Editar",
                                        on_click=editar_contato,
                                    ),
                                    ft.PopupMenuItem(
                                        text="Apagar",
                                        on_click=apagar_contato,
                                    ),
                                ]
                            )
                        )
                    ]
                )

            except Exception as ex:
                print(f"Erro ao apagar contato: {ex}")
            # Lógica para apagar o contato
            #print(f"Apagar contato: {cartao.nome}")

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
                            ft.PopupMenuItem(
                                text="Editar",
                                on_click=editar_contato,
                            ),
                            ft.PopupMenuItem(
                                text="Apagar",
                                on_click=apagar_contato,
                            ),
                        ]
                    )
                )
            ]
        )


'''
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
'''