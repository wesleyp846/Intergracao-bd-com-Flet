import flet as ft

def main(page: ft.Page):
    page.title = "Agenda de Contatos"
    page.padding = 10
    page.window_width = 400
    page.window_height = 650
    page.update()

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",    
                [   
                    ft.AppBar(title=ft.Text("AGENDA"), bgcolor=ft.colors.SURFACE_VARIANT, center_title=True),
                    ft.ElevatedButton("Mostar Contatos", on_click=lambda _: page.go("/mostar_contatos"), width=170),
                    ft.ElevatedButton("Buscar Contatos", on_click=lambda _: page.go("/buscar_contatos"), width=170),
                    ft.ElevatedButton("Incluir Contato", on_click=lambda _: page.go("/incluir_contato"), width=170),
                    ft.ElevatedButton("Editar Contato", on_click=lambda _: page.go("/editar_contato"), width=170),
                    ft.ElevatedButton("Excluir Contato", on_click=lambda _: page.go("/excluir_contato"), width=170),
                    ft.ElevatedButton("Salvar Contato", on_click=lambda _: page.go("/salvar_contato"), width=170),
                    ft.ElevatedButton("Importar Contatos", on_click=lambda _: page.go("/importar_contatos"), width=170),
                    ft.ElevatedButton("Exportar Contatos", on_click=lambda _: page.go("/exportar_contatos"), width=170),
                ],
                horizontal_alignment = ft.CrossAxisAlignment.CENTER,
            )
        )
        
        if page.route == "/mostar_contatos":
            page.views.append(
                ft.View(
                    "/mostar_contatos",
                    [
                        ft.AppBar(title=ft.Text("Mostar Contatos"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("pesquisa", on_click=lambda _: page.go("/")),
                        ft.ElevatedButton("Card de  listView contatos", on_click=lambda _: page.go("/")),
                        ft.ElevatedButton("Pagina Inicial", on_click=lambda _: page.go("/")),
                    ],
                    
                    horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                    #vertical_alignment=ft.MainAxisAlignment.END,
                )
            )

        if page.route == "/buscar_contatos":
            page.views.append(
                ft.View(
                    "/buscar_contatos",
                    [
                        ft.AppBar(title=ft.Text("Buscar Contatos"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Pagina Inicial", on_click=lambda _: page.go("/")),
                    ],
                    horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                )
            )

        if page.route == "/incluir_contato":
            buttons_row = ft.Row([
                # FAZER LOGICA DE SALVAR O CONTATO
                ft.ElevatedButton("Salvar Contato", on_click=lambda _: page.go("/"), width=170),
                ft.ElevatedButton("Cancelar", on_click=lambda _: page.go("/"), width=170)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            )
            page.views.append(
                ft.View(
                "/incluir_contato",
                [
                    ft.AppBar(title=ft.Text("Incluir Contato")),
                    ft.TextField(label="Nome", border_radius=10),
                    ft.TextField(label="Telefone", border_radius=10),
                    ft.TextField(label="E-mail", border_radius=10), 
                    ft.TextField(label="Endereço", border_radius=10),
                    buttons_row,
                ]
                )
            )

        if page.route == "/editar_contato":
            page.views.append(
                ft.View(
                    "/editar_contato",
                    [
                        ft.AppBar(title=ft.Text("Editar Contato"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Pagina Inicial", on_click=lambda _: page.go("/")),
                    ],
                    horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                )
            )

        if page.route == "/excluir_contato":
            page.views.append(
                ft.View(
                    "/excluir_contato",
                    [
                        ft.AppBar(title=ft.Text("Excluir Contato"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Pagina Inicial", on_click=lambda _: page.go("/")),
                    ],
                    horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                )
            )

        if page.route == "/salvar_contato":
            page.views.append(
                ft.View(
                    "/salvar_contato",
                    [
                        ft.AppBar(title=ft.Text("Salvar Contato"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Pagina Inicial", on_click=lambda _: page.go("/")),
                    ],
                    horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                )
            )

        if page.route == "/importar_contatos":
            page.views.append(
                ft.View(
                    "/importar_contatos",
                    [
                        ft.AppBar(title=ft.Text("Importar Contatos"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Pagina Inicial", on_click=lambda _: page.go("/")),
                    ],
                    horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                )
            )

        if page.route == "/exportar_contatos":
            page.views.append(
                ft.View(
                    "/exportar_contatos",
                    [
                        ft.AppBar(title=ft.Text("Exportar Contatos"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Pagina Inicial", on_click=lambda _: page.go("/")),
                    ],
                    horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                )
            )

        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
        

ft.app(target=main, view=ft.AppView.WEB_BROWSER)