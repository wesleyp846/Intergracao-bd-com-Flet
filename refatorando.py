import flet as ft
from flet import *
from classes import Dados

casa = True

def main(page: ft.Page):
    page.title = "Agenda de Contatos"
    page.padding = 10
    page.window_width = 400
    page.window_height = 650
    page.theme_mode = ft.ThemeMode.DARK
    page.scroll = ft.ScrollMode.AUTO

    db = Dados('banco.db')

    def renderizar_contatos():
        listagem_contatos.controls.clear()
        dados_lidos = db.ler_dados()

        for lido in dados_lidos:
            card_contato = Card(
                Container(
                    content=Column([
                        ft.ExpansionTile(
                            title=ft.Text(f"{lido[1]}"),
                            subtitle=ft.Text(f"{lido[2]}"),
                            affinity=ft.TileAffinity.LEADING,
                            initially_expanded=True,
                            collapsed_text_color=ft.colors.BLUE,
                            text_color=ft.colors.BLUE,
                            controls=[
                                Text(f"{lido[1]}"),
                                ft.ListTile(title=ft.Text(f"{lido[3]}")),
                                ft.ListTile(title=ft.Text(f"{lido[4]}")),
                            ],
                        ),
                        ft.Row([
                            ft.TextButton(
                                "Editar",
                                on_click=lambda _, nome=lido[1]: edita_contato(nome),
                            ), 
                            ft.TextButton(
                                "Apagar",
                                on_click=lambda _, nome=lido[1]: deleta_contato(nome),
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.END),
                    ]),
                    width=400,
                    padding=10,
                )
            )
            listagem_contatos.controls.append(card_contato)
        page.update()

    def deleta_contato(nome):
        db = Dados('banco.db')
        db.deletar_dados(nome)
        print("fazer uma snakBar avisando que o contato: {nome} foi excluido")
        renderizar_contatos()

    def edita_contato(nome):
        print(f'fazer a edição de {nome}')

    barra_inicial = ft.Row([
        Icon(
            icons.MENU_BOOK, 
            color='blue600',
            size=60,
        ),
        Text(
            'AGENDA', 
            size=30, 
            weight='bold',
        )
    ],
    alignment=ft.MainAxisAlignment.CENTER
    )

    listagem_contatos = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)

    renderizar_contatos()

    page.navigation_bar = NavigationBar(
        destinations=[
            NavigationDestination(
                icon=icons.CONTACT_PHONE_SHARP, 
                label="Add Contato"
            ),
            NavigationDestination(
                icon=icons.KEYBOARD_DOUBLE_ARROW_UP_SHARP, 
                label="Importar"
            ),
            NavigationDestination(
                icon=icons.KEYBOARD_DOUBLE_ARROW_DOWN_SHARP, 
                label="Exportar"
            ),
        ]
    )

    page.add(
        Column([
            barra_inicial,
            listagem_contatos,
        ])
    )

ft.app(target=main) if casa else ft.app(target=main, view=ft.AppView.WEB_BROWSER)