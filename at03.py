import flet as ft

def main(page: ft.Page):
    page.title = "Meu App"
    page.bgcolor = "#FFFFFF"
    page.window.width = 320
    page.window.height = 600
    page.padding = 20

    caixa_texto = ft.TextField(
        label="Digite seu nome"
    )

    checkbox = ft.Checkbox(
        label="Aceito os termos"
        
    )

    def enviar(e):
        page.add(
            ft.Text(f"Obrigado, {caixa_texto.value}!")
        )

    enviar_button = ft.ElevatedButton(
        content="Enviar",
        on_click=enviar
    )

    page.add(
        ft.Column(
            [
                caixa_texto,
                checkbox,
                enviar_button
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

ft.run(main)