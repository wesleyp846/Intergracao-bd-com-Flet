import flet as ft

def main(page):
    page.title = "Card Example"
    page.add(
        ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.ALBUM),
                            title=ft.Text("The Enchanted Nightingale"),
                            subtitle=ft.Text(
                                "Music by Julie Gable. Lyrics by Sidney Stein."
                            ),
                        ),
                        ft.Row(
                            [ft.TextButton("Buy tickets"), ft.TextButton("Listen")],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                    ]
                ),
                width=400,
                padding=10,
            )
        )
    )

ft.app(target=main)



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

#ft.app(target=main, view=ft.AppView.WEB_BROWSER)
