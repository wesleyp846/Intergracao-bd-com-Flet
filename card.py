import flet as ft

def card_expansivel(contato='contato', tel='contato', email='contato', endereco='contato'):
    return ft.ExpansionTile(
        leading=ft.Icon(ft.icons.CONTACT_PHONE),
        title=ft.Text(contato),
        subtitle=ft.Text(tel),
        trailing=ft.Icon(ft.icons.ARROW_DROP_DOWN),
        controls=[
            ft.ListTile(
                title=ft.Text(email),
                subtitle=ft.Text(endereco)
            )
        ]
    )