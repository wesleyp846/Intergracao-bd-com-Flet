import flet as ft
from db import dbcomando

def main(page: ft.Page):
    page.title = "Agenda de Contatos"
    page.padding = 10
    page.window_width = 400
    page.window_height = 650
    page.theme_mode = ft.ThemeMode.DARK
    db = dbcomando('banco.db')

    def salva_contato(e):
        try:
            texto_saida = [(nome.value, tel.value, email.value, endereco.value),]
            db.comando.executemany(f"""INSERT INTO contatos (nome, tel, email, endereco) VALUES (?, ?, ?, ?)""", texto_saida)
            todos=db.ler_dados('contatos')
            print(todos)

            db.conexao.commit()

            #texto_saida = [(nome.value, tel.value, email.value, endereco.value),]
            # print("Valores a serem inseridos:", texto_saida)
            #db.inserir_dados('contatos', 'nome', 'tel', 'email', 'endereco', texto_saida)
            # db.inserir_dados('contatos', 'nome', 'tel', 'email', 'endereco',)
        
            page.update()
        except Exception as ex:
            print(f"Erro ao salvar no banco de dados: {ex}")
    
    bt_salvar = ft.ElevatedButton(text='Salvar', on_click=salva_contato)
    
    nome = ft.TextField(label='Nome', border_radius=10)
    tel = ft.TextField(label='Telefone', border_radius=10)
    email = ft.TextField(label='E-mail', border_radius=10)
    endereco = ft.TextField(label='Endereço', border_radius=10)

    page.add(nome, tel, email, endereco, bt_salvar)

ft.app(target=main, view=ft.AppView.WEB_BROWSER)