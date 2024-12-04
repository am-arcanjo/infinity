import flet as ft

#Não funciona
def principal(page: ft.Page):
    iterador1 = 0
    iterador2 = 0
    def teclado(evento: ft.KeyboardEvent):
        iterador1 = 0
        iterador2 = 0
        if evento.key.lower() == "a":
            iterador1 += 1
        elif evento.key.lower() == "l":
            iterador2 += 1
    page.on_keyboard_event = teclado
    
    jogador1 = ft.Text(f"Jogador 1: {iterador1}")
    jogador2 = ft.Text(f"Jogador 2: {iterador2}")
    
    page.add(jogador1, jogador2)
    
ft.app(target=principal)