import flet as ft
from db import dbcomando

def main(page: ft.Page):
    page.add()

ft.app(target=main, view=ft.AppView.WEB_BROWSER)