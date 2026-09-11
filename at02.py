import flet as ft

def main(page: ft.Page):
    page.title = "Meu App"
    page.bgcolor = "#CDCACA"
    page.window.width = 320
    page.window.height = 600
    page.padding = 20

    nome = ft.Text(
        "Enzo Avanze",
        size=25,
        color="#00d5ff"
    )

    subtitulo = ft.Text(
        "Bem-vindo ao nosso aplicativo!",
        size=15,
        color="#00d5ff"
    )

    email = ft.Text(
        "avanze@gmail.com",
        size=15,
        color="#FFFFFF"
    )

    telefone = ft.Text(
        "Telefone: (11) 99999-9999",
        size=15,
        color="#FFFFFF"
    )

    page.add(
        ft.Container(
            content=ft.Column(
                [
                    nome,
                    subtitulo,

                    ft.Row(
                        [
                            ft.Icon(ft.Icons.EMAIL, color="#00d5ff"),
                            email
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),

                    ft.Row(
                        [
                            ft.Icon(ft.Icons.PHONE, color="#00d5ff"),
                            telefone
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            bgcolor="#0F0063",
            padding=20,
            border_radius=10
        )
    )

ft.run(main)