import flet as ft

def card_de_contato(contato, tel):
    return ft.Container(
        content=ft.Column(
            [
                ft.ListTile(
                    leading=ft.Icon(ft.icons.CONTACT_PHONE),
                    title=ft.Text(contato),
                    subtitle=ft.Text(
                        tel
                    ),
                ),
                ft.Row([
                        ft.TextButton('Ver contato'), 
                        ft.ElevatedButton("Pagina Inicial", on_click=lambda _: page.go("/")),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ]
        ),
        width=400,
        padding=10,
    )


def main(page):
    page.title = 'Exemplo de card'
    page.add(
        ft.Card(
            card_de_contato('Nome do contato', 'Telefone da pessoa')
        )
    )

ft.app(target=main, view=ft.AppView.WEB_BROWSER)



# def Card(expanded=False):
#     card = ft.Container(
#         children=[
#             ft.Text("Título do Card"),
#             ft.Container(width=20),
#             ft.IconButton(ft.icons.CHEVRON_RIGHT_SHARP, on_click=lambda e: toggle_card(card)),
#         ],
#         width=300,
#         height=150,
#         bgcolor=ft.colors.SURFACE_VARIANT,
#         border_radius=10,
#         padding=15,
#         expand=expanded,
#     )

#     return card

# def toggle_card(card):
#     card.expand = not card.expand
#     card.update()

# def main(page):  
#     page.add(Card())
