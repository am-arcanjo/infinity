import flet as ft

def principal(page: ft.Page):
    campo_nome = ft.TextField(label="Digite seu nome: ")

    def cumprimentar_usuario(evento):
        nome = campo_nome.value
        mensagem = ft.Text(f"Olá {nome}")
        page.add(mensagem)

    enviar = ft.ElevatedButton("Enviar", on_click=cumprimentar_usuario)

    page.add(campo_nome, enviar)

ft.app(target=principal)