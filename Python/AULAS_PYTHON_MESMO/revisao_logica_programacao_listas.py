# LISTAS > conjunto de variáveis, valores, etc
# Usa-se [] para 'introduzir' uma
# Temos métodos úteis tais como .append() para adicionar um elemento ao final da lista


# Exemplo qualquer:
# lista_afazeres = ['acordar', 'existir', 'não desistir']

# for afazer in lista_afazeres:
#     print(afazer)


#DESAFIO: Vocês devem criar um jogo onde o jogador precisa encontrar o "tesouro" escondido em um mapa representado por uma lista de listas (matriz). O jogador pode escolher uma posição para cavar e descobrir se encontrou o tesouro.

import random

treasureList = [[],[],[]]

random_column = random(range(1,4)) 
random_line = random(range(1,4))

guess_column = int(input("Digite a coluna na qual você acha que o tesouro está: "))
guess_line = int(input("Digite a linha na qual você acha que o tesouro está: "))

while guess_column != random_column and guess_line != guess_line:
    

