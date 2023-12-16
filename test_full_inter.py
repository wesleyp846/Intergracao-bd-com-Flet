import flet as ft
from flet import *
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

    def create_main_view():
        return ft.View(
            "/",
            [
                ft.AppBar(title=ft.Text("AGENDA"), bgcolor=ft.colors.SURFACE_VARIANT, center_title=True),
                ft.ElevatedButton("Mostar Contatos", on_click=lambda _: page.push(create_mostrar_contatos_view()), width=170),
                ft.ElevatedButton("Incluir Contato", on_click=lambda _: page.push(create_incluir_contato_view()), width=170),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

    def create_mostrar_contatos_view():
        dados = db.ler_dados()
        cards = [Card.card_expansivel(card[1], card[2], card[3], card[4]) for card in dados]
        return ft.View(
            "/mostar_contatos",
            [
                ft.AppBar(title=ft.Text("Mostrar Contatos"), bgcolor=ft.colors.SURFACE_VARIANT),
                ft.ElevatedButton("Pesquisa", on_click=lambda _: page.pop(), width=170),
                *cards,
                ft.ElevatedButton("Página Inicial", on_click=lambda _: page.pop()),
            ],
            scroll=ft.ScrollMode.AUTO,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

    def create_incluir_contato_view():
        def salvar_contato(nome, tel, email, endereco):
            db.salvar_dados(nome, tel, email, endereco)

        name = ft.TextField(label="Nome", border_radius=10)
        phone = ft.TextField(label="Telefone", border_radius=10)
        mail = ft.TextField(label="E-mail", border_radius=10)
        address = ft.TextField(label="Endereço", border_radius=10)

        buttons_row = ft.Row(
            [
                ft.ElevatedButton("Salvar Contato", on_click=lambda _: salvar_contato(name.value, phone.value, mail.value, address.value)),
                ft.ElevatedButton("Cancelar", on_click=lambda _: page.pop(), width=170),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )

        return ft.View(
            "/incluir_contato",
            [
                ft.AppBar(title=ft.Text("Incluir Contato")),
                name,
                phone,
                mail,
                address,
                buttons_row,
            ],
        )

    page.push(create_main_view())
    page.on_view_pop = lambda view: page.go(view.route)

ft.app(target=main) if casa else ft.app(target=main, view=ft.AppView.WEB_BROWSER)