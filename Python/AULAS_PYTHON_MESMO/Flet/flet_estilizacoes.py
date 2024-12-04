import flet as ft

def principal(page: ft.Page):
    iterador = 1
    
    def button_click(e):
        nonlocal iterador
        if iterador % 2 != 0:
                button.style.bgcolor = ft.colors.GREEN
                button.style.color = ft.colors.ORANGE
        else:
                button.style.bgcolor = ft.colors.AMBER_300
                button.style.color = ft.colors.LIGHT_BLUE_600
        
        iterador += 1
        e.control.update()   
    
    button = ft.TextButton(
    text = "Oi, clique em mim",
    on_click = button_click,
    style = ft.ButtonStyle
    (bgcolor = ft.colors.AMBER_300,
     color = ft.colors.LIGHT_BLUE_600),
    width = 200,
    height = 100
    )
    
    page.add(button)

ft.app(target=principal)