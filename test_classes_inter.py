import flet as ft
from classes import Dados
import logging

logging.basicConfig(filename='app.log', level=logging.DEBUG)

def main(page: ft.Page):
    page.title = "Agenda de Contatos"
    page.padding = 10
    page.window_width = 400
    page.window_height = 650
    page.theme_mode = ft.ThemeMode.DARK
    db = Dados('banco.db')

    def salva_contato(nome, tel, email, endereco):
        db.salvar_dados(nome, tel, email, endereco)
    
    def apaga_contato(nome):
        db.deletar_dados(nome)

    nome = ft.TextField(label='Nome', border_radius=10)
    tel = ft.TextField(label='Telefone', border_radius=10)
    email = ft.TextField(label='E-mail', border_radius=10)
    endereco = ft.TextField(label='Endereço', border_radius=10)

    bt_salvar = ft.ElevatedButton(
        text='Salvar',
        on_click=lambda _: salva_contato(nome.value, tel.value, email.value, endereco.value)
    )

    bt_apaga = ft.ElevatedButton(
        text='Apaga',
        on_click=lambda _: apaga_contato(nome.value)
    )

    page.add(nome, tel, email, endereco, bt_salvar, bt_apaga)

ft.app(target=main)