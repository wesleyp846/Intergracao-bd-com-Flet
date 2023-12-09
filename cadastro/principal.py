import flet as ft
from flet import *
import random
import datetime
import os

casa=True

now=datetime.datetime.now()
formated_data=now.strftime('%d-%m-%Y')

def main(page:ft.Page):
    page.theme_mode='dark'
    page.scroll = 'auto'
    page.window_width = 600
    page.window_height = 700

    all_food = Column()

    def addtofood(e):
        random_price=random.randint(50,100)
        total_price=random_price * int(con_input.content.controls[4].value)
        all_food.controls.append(
            Container(
                padding=10,
                bgcolor='green200',
                content=Column([
                    #pegando o valor de con_input o terceiro valor que é 'Nome comida'
                    Text(con_input.content.controls[3].value,
                        weight='bold',
                        color='black',
                        size=20
                    ),
                    
                    Text(f'Total da compra {con_input.content.controls[4].value}',
                        weight='bold',
                        color='black',
                        size=20
                    ),

                    Row([
                        Text('Total a pagar', width='bold',color='black'),
                        Text(f"R${'{:,.2f}'.format(total_price)}",color='black')
                    ], alignment='spaceBetween')
                ])
            )
        )

        page.update()

    con_input = Container(
        content=Column([
            TextField(label='Nome do usuario'),
            TextField(label='Endereço'),
            Text('faça seu pedido', size=25,weight='bold'),
            TextField(label='Nome comida'),
            TextField(label='Compra por peças'),
            ElevatedButton(
                'Cadastrar o pedido',
                on_click=addtofood
            )
        ])
    )

    def buildmeupedido(e):
        mdialog=AlertDialog(
            title=Text(
                'Nota dos pedidos',
                weight='blod',
                size=30,
                ),

            content=Column([
                Row([
                    Text(con_input.content.controls[0].value,
                        weight='bold',
                        color='black',
                        size=25
                    ),
                    Text(f'Data do pedido: {formated_data}',
                        weight='bold',
                        color='black',
                        size=25
                    )
                ]),
                
                Text(con_input.content.controls[1].value,
                    weight='bold',
                    color='black',
                    size=25,
                    text_align='start'
                ),

                Row([
                    Text('Endereço do cliente',
                        weight='bold',
                        color='black',
                        size=25
                    ),
                    Text(con_input.content.controls[1].value,
                        weight='bold',
                        color='black',
                        size=25
                    ),
                ], alignment='end'),
                
                Text(
                    'Seus pedidos',
                    weight='bold',
                    color='black',
                    size=25
                ),
                
                all_food
            ])    
        )
        page.dialog=mdialog
        mdialog.open=True
        page.update()

    page.floating_action_button = FloatingActionButton(
        icon='add', 
        bgcolor='blue',
        on_click=buildmeupedido 
    )

    page.add(
        Column([
            con_input,
            Text('Lista de pedidos', size=20,weight='bold'),
            all_food
        ])
    )
    

ft.app(target=main) if casa else ft.app(target=main, view=ft.AppView.WEB_BROWSER)