import flet as ft

def principal(page: ft.Page):
    texto_1 = ft.Text("Pretty 🎵 🎶")
    texto_2 = ft.Text("Pretty little cemetery")
    texto_3 = ft.Text("On the street looking ordinary")
    texto_4 = ft.Text("I know that is where I'll go, when I've got shit to bury")
    
    coluna_1 = ft.Column(controls=[texto_1, texto_2])
    coluna_2 = ft.Column(controls=[texto_3, texto_4])
    
    linha = ft.Row(controls=[coluna_1, coluna_2])
    
    page.add(linha)
    
ft.app(target=principal)