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
    
        
class Reserva:
    def __init__(self, cliente: Cliente, quarto: Quarto, data):
        self.cliente = cliente
        self.quarto = quarto
        self.data = data
        self.confirmada = False
    
    def confirmar_reserva(self):
        self.confirmada = True
        self.quarto.disponibilidade = False
    
    
class GerenciadorDeReservas:
    def __init__(self, reserva: Reserva):
            self.reserva = reserva    
        

quarto_1 = Quarto(101, "Básico" , 150)
cliente_1 = Cliente("Anabella", "anna.bella@gmail.com")
