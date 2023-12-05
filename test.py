import flet as ft
from db import dbcomando

def main(page: ft.Page):
    page.title = "Agenda de Contatos"
    page.padding = 10
    page.window_width = 400
    page.window_height = 650
    page.theme_mode = ft.ThemeMode.DARK


# #Inserção
# dado = [
#     ('Maria','1556'),
# ]
# comando.execute("""INSERT INTO tabela1 (nome) VALUES (?)""", dado)
# conexao.commit()

    def salva_contato(e):
        db = dbcomando('banco.db')
        texto_saida = [(nome.value, tel.value, email.value, endereco.value,)]
        #texto_saida = [({nome.value}), ({tel.value}), ({email.value}), ({endereco.value})]
        db.inserir_dados('contatos', 'nome', 'tel', 'email', 'endereco', texto_saida)
        
        page.update()

    #texto_saida = ft.Text()
    
    bt_salvar = ft.ElevatedButton(text='Salvar', on_click=salva_contato)
    
    nome = ft.TextField(label='Nome', border_radius=10)
    tel = ft.TextField(label='Telefone', border_radius=10)
    email = ft.TextField(label='E-mail', border_radius=10)
    endereco = ft.TextField(label='Endereço', border_radius=10)

    page.add(nome, tel, email, endereco, bt_salvar)

ft.app(target=main, view=ft.AppView.WEB_BROWSER)