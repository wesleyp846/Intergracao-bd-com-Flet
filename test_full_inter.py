import flet as ft
from classes import Dados
from classes import Card

casa = True

def main(page: ft.Page):
    page.title = "Agenda de Contatos"
    page.padding = 10
    page.window_width = 400
    page.window_height = 650
    page.theme_mode = ft.ThemeMode.DARK
    page.update()
    db = Dados('banco.db')

    def route_change(route):
        page.views.clear()
        page.ro
        page.views.append(
            ft.View(
                "/",    
                [   
                    ft.AppBar(title=ft.Text("AGENDA"), bgcolor=ft.colors.SURFACE_VARIANT, center_title=True),
                    ft.ElevatedButton("Mostar Contatos", on_click=lambda _: page.go("/mostar_contatos"), width=170),
                    ft.ElevatedButton("Incluir Contato", on_click=lambda _: page.go("/incluir_contato"), width=170),
                ],
                horizontal_alignment = ft.CrossAxisAlignment.CENTER,
            )
        )
        
        if page.route == "/mostar_contatos":
            db = Dados('banco.db')
            dados=db.ler_dados()
            c=Card
            cards=[c.card_expansivel(card[1],card[2],card[3],card[4]) for card in dados]
            page.views.append(
                ft.View(
                    "/mostar_contatos",
                    [
                        ft.AppBar(title=ft.Text("Mostar Contatos"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("pesquisa", on_click=lambda _: page.go("/")),
                        *cards,
                        ft.ElevatedButton("Pagina Inicial", on_click=lambda _: page.go("/")),
                    ],
                    scroll=ft.ScrollMode.AUTO,
                    horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                )
            )
        

        if page.route == "/incluir_contato":
            db = Dados('banco.db')
            def salvar_contato(nome, tel, email, endereco):
                db.salvar_dados(nome, tel, email, endereco)

            name=ft.TextField(label="Nome", border_radius=10)
            phone=ft.TextField(label="Telefone", border_radius=10)
            mail=ft.TextField(label="E-mail", border_radius=10)
            adress=ft.TextField(label="Endereço", border_radius=10)

            # Layout dos botões
            buttons_row = ft.Row([
                ft.ElevatedButton(
                    "Salvar Contato", 
                    on_click=lambda _: salvar_contato(name.value, phone.value, mail.value, adress.value)
                ),
                ft.ElevatedButton("Cancelar", on_click=lambda _: page.go("/"), width=170)
            ], alignment=ft.MainAxisAlignment.CENTER)

            page.views.append(
                ft.View(
                    "/incluir_contato", 
                    [
                        ft.AppBar(title=ft.Text("Incluir Contato")),
                        name,
                        phone,
                        mail,
                        adress,
                        buttons_row,
                    ]
                )
            )
            page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
        
ft.app(target=main) if casa else ft.app(target=main, view=ft.AppView.WEB_BROWSER)