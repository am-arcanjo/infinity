import flet as ft

def principal(page: ft.Page):
    def clicou_botao(evento):
        texto_click = ft.Text("Você clicou no botão, obrigada.")
        page.add(texto_click)

    texto = ft.Text("Boa noite.")
    botao = ft.ElevatedButton(text="Clique aqui!", on_click=clicou_botao)
    page.add(texto, botao)

ft.app(target=principal)