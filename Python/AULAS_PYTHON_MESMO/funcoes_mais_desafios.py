# Faça um programa de calculadora simples que mostra um menu ao usuário e permita-o escolher qual operação básica este deseja realizar. Utilize funções separadas para cada operação.

# adicao = lambda num1, num2: num1 + num2
# subtracao = lambda num1, num2: num1 - num2
# multiplicacao = lambda num1, num2: num1 * num2
# divisao = lambda num1, num2: num1 / num2

# operacao_desejada = int(input("Bem-vindo à calculadora. Escolha qual das operações a seguir você deseja realizar entre dois números. \n 1 - Adição \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n"))

# num1 = int(input("Digite seu primeiro número: "))
# num2 = int(input("Agora, digite o segundo: "))

# if operacao_desejada == 1:
#     print(adicao(num1, num2))
# elif operacao_desejada == 2:
#     print(subtracao(num1, num2))
# elif operacao_desejada == 3:
#     print(multiplicacao(num1, num2))
# elif operacao_desejada == 4:
#     print(divisao(num1, num2))


# 6 - Recriar o jogo do pedra, papel e tesoura, só que utilizando funções. Deverão haver 3 funções: escolha_computador(), determinar_vencedor(), mostrar_resultado(). Respectivamente, elas devem gerar aleatoriamente uma escolha para o computador e retornar a mesma, pedir a escolha do jogador e "bater" com a do computador para ver quem venceu, mostrar ambas as escolhas e quem ganhou

import random;

def escolha_computador():
    possibilidades_pc = ["pedra", "papel", "tesoura"]
    escolha_pc = random.choice(possibilidades_pc)
    return escolha_pc

def determinar_vencedor(escolha_jogador: str, escolha_computador: str):
    computadorVence = "O computador venceu..."
    jogadorVence = "Você venceu!"
    empate = "Empate :o"
    if escolha_computador == "pedra" and escolha_jogador == "tesoura":
        return computadorVence
    elif escolha_computador == "tesoura" and escolha_jogador == "papel":
        return computadorVence
    elif escolha_computador == "papel" and escolha_jogador == "pedra":
        return computadorVence
    elif escolha_jogador == escolha_computador:
        return empate
    else:
        return jogadorVence


escolha_computador = escolha_computador()
escolha_jogador = input("Escolha entre pedra, papel e tesoura: ")

def mostrar_resultado():
    print("A escolha do computador foi: " + escolha_computador)
    print("A sua escolha foi: " + escolha_jogador)
    print(determinar_vencedor(escolha_jogador, escolha_computador))

mostrar_resultado()
