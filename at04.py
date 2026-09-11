import flet as ft


def main(page: ft.Page):
    page.title = "Meu App"
    page.bgcolor = "#16006C"
    page.window.width = 500
    page.window.height = 800
    page.padding = 20

    caixa_texto = ft.TextField(
        label="Novo item",
        bgcolor="#FFFFFF"
    )

    lista = ft.Column()


    def adicionar(e):

        quantidade = ft.Text("1", color="#FFFFFF", size=20)

        def aumentar(e):
            quantidade.value = str(int(quantidade.value) + 1)
            page.update()

        def diminuir(e):
            valor = int(quantidade.value)

            if valor > 0:
                quantidade.value = str(valor - 1)

            page.update()

        def remover(e):
            lista.controls.remove(nova_linha)
            page.update()


        aumentar_button = ft.IconButton(
            icon=ft.Icons.ADD,
            on_click=aumentar,
            icon_color="#00d5ff"
        )

        diminuir_button = ft.IconButton(
            icon=ft.Icons.REMOVE,
            on_click=diminuir,
            icon_color="#00d5ff"
        )

        remover_button = ft.IconButton(
            icon=ft.Icons.DELETE,
            on_click=remover,
            icon_color="#00d5ff"
        )

        nova_linha = ft.Row(
            [
                ft.Text(caixa_texto.value, color="#FFFFFF", size=20),
                diminuir_button,
                quantidade,
                aumentar_button,
                remover_button
            ]
        )

        lista.controls.append(nova_linha)

        caixa_texto.value = ""

        page.update()


    adicionar_button = ft.Button(
        content=ft.Text("Adicionar"),
        on_click=adicionar,
        bgcolor="#00d5ff",
        color="#FFFFFF"
    )


    page.add(
        ft.Column(
            [
                ft.Row(
                    [
                        caixa_texto,
                        adicionar_button
                    ]
                ),

                lista
            ]
        )
    )


ft.run(main)