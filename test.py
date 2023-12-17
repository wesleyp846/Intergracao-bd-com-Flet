import flet as ft
from flet import *

def main(page: ft.Page):
    page.window_width = 400
    page.window_height = 650

    def tarsformacaoapa(e):
        cartao.offset=ft.transform.Offset(0, 0)
        page.update()

    def tarsformacaodes(e):
        cartao.offset=ft.transform.Offset(0, 4)
        page.update()

    botao =  ElevatedButton(
                    'aparece',
                    on_click=tarsformacaoapa,
                )

    name=ft.TextField(label="Nome", border_radius=10,)
    phone=ft.TextField(label="Telefone", border_radius=10)
    mail=ft.TextField(label="E-mail", border_radius=10)
    adress=ft.TextField(label="Endereço", border_radius=10)
    
    cartao = Card(
        offset=ft.transform.Offset(0, 0),
        animate_offset=animation.Animation(600,curve='easyIn'),
        content=Container(
            content=Column([
                name,
                phone,
                mail,
                adress,
                ElevatedButton(
                    'desaparece',
                    on_click=tarsformacaodes,
                )
            ]),
        ),
    )
    
    page.add(
        Column([
            cartao,
            botao,
        ])
    )

ft.app(target=main)