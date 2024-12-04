# Projeto de Reserva de Hotel

import flet as ft


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
    def __init__(self):
            self.Lista_de_reservas = []
            self.lista_de_quartos = []   
    
    def adicionar_quarto(self, quarto: Quarto):
        self.lista_de_quartos.append(quarto)
       
    def listar_quartos_disponiveis(self):
        quartos_disponiveis = []
        for quarto in self.lista_de_quartos:
            if quarto.disponibilidade:
                quartos_disponiveis.append(quarto)
        print(quartos_disponiveis)
    
    def criar_reserva(self, cliente: Cliente, data, numero_quarto):
        quarto_reservado = None
        
        for quarto in self.lista_de_quartos:
            if quarto.disponibilidade == True and quarto.numero == numero_quarto:
                quarto_reservado = quarto   
                return quarto_reservado
        
        if quarto_reservado != None:
            reserva_do_quarto = Reserva(cliente, quarto, data)
            self.lista_de_reservas.append(reserva_do_quarto)
            reserva_do_quarto.confirmar_reserva()
            return reserva_do_quarto
        
cliente_1 = Cliente("Anabella", "anna.bella@gmail.com")
    
    
def principal(page: ft.Page):
    # Inicializador do gerenciador de reservas
    gerenciador_hotel = GerenciadorDeReservas()
    quarto_1 = Quarto(101, "Básico", 150)
    quarto_2 = Quarto(201, "Deluxe", 250)
    quarto_3 = Quarto(301, "Premium", 350)
    
    gerenciador_hotel.adicionar_quarto(quarto_1)
    gerenciador_hotel.adicionar_quarto(quarto_2)
    gerenciador_hotel.adicionar_quarto(quarto_3)

    
    # Seção visual de entradas do cliente
    nome_cliente = ft.TextField(label = "Nome do cliente", width = 300)
    email_cliente = ft.TextField(label = "E-mail do cliente", width = 300)
    numero_quarto = ft.TextField(label = "Número do quarto", width = 300)
    data = ft.TextField(label = "Data (Formato: AAAA-MM-DD)", width = 300)
    
    lista_quartos = ft.Column()
    status = ft.Text()
    
    # Funções
    def reservar_quarto(evento):
        print(nome_cliente.value)
        print(email_cliente.value)
        cliente_informado = Cliente(nome_cliente.value, email_cliente.value)
        numero_quarto_informado = int(numero_quarto.value)
        data_informada = data.value
        reserva = gerenciador_hotel.criar_reserva(cliente_informado, numero_quarto_informado, data_informada)
        
        if reserva != None:
            status.value = "A sua reserva deu certo!"
        else:
            status.value = "O quarto escolhido não têm disponibilidade."
    
    page.add(
        ft.Column([
            ft.Text("Sistema de Reservas do Hotel", size = 45.5),
            lista_quartos,
            ft.Row([nome_cliente, email_cliente]),
            ft.Row([numero_quarto, data]),
            ft.ElevatedButton("Reservar Quarto", on_click=reservar_quarto),
            status
        ])
    )

ft.app(target=principal)   
    
