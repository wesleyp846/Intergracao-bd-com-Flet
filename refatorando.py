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

    db=Dados('banco.db')

    def deleta_contato(e):
        #print(f"Apagar contato: {e.control.content.value}")
        #print(f"Apagar contato: {contato}")
        #contato = e.control.parent.title.value 
        #contato = listagem_contatos.controls.Card.title.value
        #contato = listagem_contatos.controls[0].content.content.controls[0]
        contato = listagem_contatos.controls[0].content.content.controls[0].controls[0].value
        print(f"Apagar contato: {contato}")
   
    barra_menu = Text(
        'Todos os elatede botes aqui', 
        size=20, 
        weight='bold',
        bgcolor='red'
    )

    listagem_contatos = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
    dados_lidos = db.ler_dados()
    
    for lido in dados_lidos:
        listagem_contatos.controls.append(
            Card(
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
                            #para apagar o dado é o nome
                            ft.TextButton("Editar"), 
                            ft.TextButton(
                                "Apagar",
                                on_click = deleta_contato, #lambda _: db.deletar_dados(lido[1]),
                            ),
                        ],alignment=ft.MainAxisAlignment.END,
                        ),
                    ]
                ),
                width=400,
                padding=10,
            )
        )
    )

    page.add(
        Column([
            barra_menu,
            listagem_contatos,
        ])
    )

ft.app(target=main) if casa else ft.app(target=main, view=ft.AppView.WEB_BROWSER)
