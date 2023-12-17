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
                            affinity=ft.TileAffinity.LEADING,
                            initially_expanded=True,
                            collapsed_text_color=ft.colors.BLUE,
                            text_color=ft.colors.BLUE,
                            controls=[
                                ft.ListTile(title=ft.Text(f"Telefone: {lido[2]}")),
                                ft.ListTile(title=ft.Text(f"E-mail: {lido[3]}")),
                                ft.ListTile(title=ft.Text(f"Endereço: {lido[4]}")),
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

    def adicionar_contato():
        print("Função para adicionar contato")

    def importar_dados():
        print("Função para importar dados")

    def exportar_dados():
        print("Função para exportar dados")

    def barra_final(selected_index):
        objeto=selected_index.data
    
        if objeto == '0':
            print('Add Contato')
            Card(
                content=Container(
                    content=Column([
                        Text('Novo cadastro',size=20,weight='bold'),
                    ])
                )
            )
            page.add(Card)
            # return Card(
            #     offset=transform.Offset(0,0),
            #     animate_offset=animation.Animation(600,curve='easyIn'),
            #     elevation=30,
            #     content=Container(
            #         bgcolor='green200',
            #         content=Column([
            #             Row([
            #                 Text('Novo cadastro',size=20,weight='bold'),
            #                 IconButton(icon='close',icon_size=30), #on_click=hidecon),
            #             ]),
            #         #     name,
            #         #     age, 
            #         #     contact,
            #         #     gender, 
            #         #     email, 
            #         #     address,
            #         #     FilledButton('Salvar dados', on_click=savedata)
            #         ])
            #     )
            # )
        
        if objeto == '1':
            print('Importar')
        if objeto == '2':
            print('Exportar')

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
                label="Add Contato",
                #on_select=adicionar_contato
            ),
            NavigationDestination(
                icon=icons.KEYBOARD_DOUBLE_ARROW_UP_SHARP, 
                label="Importar"
            ),
            NavigationDestination(
                icon=icons.KEYBOARD_DOUBLE_ARROW_DOWN_SHARP, 
                label="Exportar"
            ),
        ],
        on_change=barra_final
    )

    page.add(
        Column([
            barra_inicial,
            listagem_contatos,
        ])
    )

ft.app(target=main) if casa else ft.app(target=main, view=ft.AppView.WEB_BROWSER)