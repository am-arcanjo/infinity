# Desafio é fazer com flet e POO com classes e herança um, joguinho de clickar num botão e atacar o vilão

import random
import flet as ft

def principal(page: ft.Page):
    botao_ataque = ft.ElevatedButton(label="Atacar!")

    def atacar(evento):
        ...
        #fazer lógica

    page.add(botao_ataque)

ft.app(target=principal)


class Personagem:
    def __init__(self, nome, ataque, vida):
        self.nome = nome
        self.ataque = ataque
        self.vida = vida

# Lembrar de fazer lógica pra quando derrotar o vilão