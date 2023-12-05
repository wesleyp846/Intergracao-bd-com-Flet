import flet as ft

def card_expansivel(nome='Nome', tel='Telefone', email='E-mail:', endereco='Endereço:'):
        return ft.ExpansionTile(
            leading=ft.Icon(ft.icons.CONTACT_PHONE),
            title=ft.Text(nome),
            subtitle=ft.Text(tel),
            trailing=ft.Icon(ft.icons.ARROW_DROP_DOWN),
            controls=[
                ft.ListTile(
                    title=ft.Text(email),
                    subtitle=ft.Text(endereco)
                )
            ]
        )