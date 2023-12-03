import flet as ft

def main(page: ft.Page):
    page.title="Agenda de Contatos"
    page.bgcolor=ft.colors.BLACK
    page.window_width = 400
    page.window_height = 650
    page.update()


ft.app(target=main, view=ft.WEB_BROWSER)