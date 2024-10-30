#Projeto de Reserva de Hotel

# import flet as ft

# def principal(page: ft.Page):
     
#     page.add()

# ft.app(target=principal)



class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email


class Quarto:
    def __init__(self, numero, tipo, preco):
        self.numero = numero
        self.tipo = tipo
        self.preco = preco
        self.disponibilidade = True
        
#class Reserva(Cliente, Quarto):
#    def __init__():
        

quarto_1 = Quarto(101, "Básico" , 150)
cliente_1 = Cliente("Anabella", "anna.bella@gmail.com")