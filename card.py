import flet as ft
from db import dbcomando

def card_expansivel(nome='Nome', tel='Telefone', email='E-mail:', endereco='Endereço:'):
        return ft.ExpansionTile(
            leading=ft.Icon(ft.icons.CONTACT_PHONE),
            title=ft.Text(nome),
            #title=ft.Text(dado[1]),
            subtitle=ft.Text(tel),
            #subtitle=ft.Text(dado[2]),
            trailing=ft.Icon(ft.icons.ARROW_DROP_DOWN),
            controls=[
                ft.ListTile(
                    title=ft.Text(email),
                    #title=ft.Text(dado[3]),
                    subtitle=ft.Text(endereco)
                    #subtitle=ft.Text(dado[4])
                )
            ]
        )