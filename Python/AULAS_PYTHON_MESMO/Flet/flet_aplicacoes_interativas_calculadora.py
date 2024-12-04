import flet as ft

def principal(page: ft.Page):
    introducao = ft.Text("Digite dois números para operarmos em cima")
    numero1 = ft.TextField(label="1º Número: ")
    numero2 = ft.TextField(label="2º Número: ")
    mostrar_resultado = ft.Text("")

    def somar(evento):
        n1 = int(numero1.value)
        n2 = int(numero2.value)
        resultado = n1 + n2
        mostrar_resultado.value = str(resultado)
        page.update()

    def subtrair(evento):
        n1 = int(numero1.value)
        n2 = int(numero2.value)
        resultado = n1 - n2
        mostrar_resultado.value = str(resultado)
        page.update()


    def dividir(evento):
        n1 = int(numero1.value)
        n2 = int(numero2.value)
        resultado = n1 / n2
        mostrar_resultado.value = str(resultado)
        page.update()


    def multiplicar(evento):
        n1 = int(numero1.value)
        n2 = int(numero2.value)
        resultado = n1 * n2
        mostrar_resultado.value = str(resultado)
        page.update()
    
    btn_soma = ft.ElevatedButton(text="+", on_click=somar)
    btn_subtrair = ft.ElevatedButton(text="-", on_click=subtrair)
    btn_multiplicar = ft.ElevatedButton(text="*", on_click=multiplicar)
    btn_dividir = ft.ElevatedButton(text="/", on_click=dividir)

    page.add(introducao, numero1, numero2, btn_soma, btn_dividir, btn_multiplicar, btn_subtrair, mostrar_resultado)


ft.app(target=principal)