# Clássico jogo do Sílvio Santos das 3 pistas. A ideia é que o usuário adivinhe uma palavra em 3 tentativas, e a cada tentativa errada, seja fornecida uma dica. Se ele exaurir as dicas, e mesmo assim não acertar, ele perde.
# O professor reformulou tal que a ideia é competir com um segundo jogador.
# O jogador 1 receberá a primeira dica e tentará acertar. Caso não acerte, o jogo irá para o jogador 2 que tentará acertar após receber a segunda dica (e saber a primeira). Após isso, caso ainda não acerte, o jogador 1 receberá a terceira dica e tentará acertar. Se não der certo, o joador 2 tenta com todas as três dicas. Se nem assim for, ambos perdem.

# Fazer outra versão em que o "momento" de acerto dá pontos diferentes, ou seja, se o jogador acertar na primeira dica, ele ganhará mais pontos do que no caso dele acertar somente na segunda ou na terceira dica. E cada round consiste com um jogador iniciando. Ou seja, se no primeiro round, o jogador 1 iniciar, o segundo round quem inicia é o jogador 2. Ao final dos 10 rounds, ganha quem tem mais pontos.

################# VERSÃO 1

# import random

# dicionario = {
#     "machado": {
#         1: "é um sobrenome",
#         2: "corta madeira",
#         3: "de assis"
#     },
#     "são paulo": {
#         1: "nome de santo",
#         2: "nome de cidade",
#         3: "nome de time"
#     },
#     "planeta": {
#         1: "o sol não é",
#         2: "a lua não é",
#         3: "a terra é"
#     },
#     "sanfona": {
#         1: "instrumento musical",
#         2: "fole",
#         3: "luiz gonzaga"
#     },
#     "águia": {
#         1: "ave com bico",
#         2: "carnivora",
#         3: "garras"
#     },
#     "alergia": {
#         1: "poeira",
#         2: "tinta",
#         3: "doença"
#     },
#     "açúcar": {
#         1: "cana",
#         2: "beterraba",
#         3: "cristais"
#     },
#     "áfrica": {
#         1: "antigo continente",
#         2: "deserto do saara",
#         3: "leões e elefantes"
#     },
#     "adolescente": {
#         1: "rebelde",
#         2: "irresponsável",
#         3: "quase adulto"
#     },
#     "aeroporto": {
#         1: "pista",
#         2: "hangar",
#         3: "avião"
#     },
#     "agricultura": {
#         1: "terra",
#         2: "cultivo",
#         3: "camponês"
#     },
#     "neblina": {
#         1: "nevoeiro",
#         2: "trevas",
#         3: "nuvens"
#     },
#     "edifício": {
#         1: "construção",
#         2: "apartamentos",
#         3: "arranha-céu"
#     },
#     "flauta": {
#         1: "instrumento musical",
#         2: "buracos",
#         3: "sopro"
#     }
# }

# palavra, dicas = random.choice(list(dicionario.items()))

# print("Vamos começar nosso jogo, vocês receberão dicas para tentar acertar uma palavra!")
# acertou = False
# iterador = 1

# while acertou == False and iterador <= 3:
#     print(f"A primeira dica é: {dicas[iterador]}")
#     chute1 = input("Jogador 1, tente acertar a palavra: ")
#     if chute1 == palavra:
#         print("Jogador 1, você venceu!")
#         acertou = True
#     else:
#         print(f"\nJogador 2, agora é sua vez de tentar acertar a palavra. \nA primeira dica foi: {dicas[iterador]}.")
#         iterador += 1 
#         print(f"E a segunda dica é {dicas[iterador]}.")
#         chute2 = input("Qual seu chute?: ")
#         if chute2 == palavra:
#             print("Jogador 2, você venceu!")
#             acertou = True
#         else:
#             print(f"\nJogador 1, agora é sua vez de tentar acertar a palavra. \nA primeira dica foi {dicas[iterador - 1]}. \nA segunda dica foi: {dicas[iterador]}.")
#             iterador += 1
#             print(f"E a terceira dica é {dicas[iterador]}.")
#             chute3 = input("Tente acertar a palavra, Jogador 1!: ")
#             if chute3 == palavra:
#                 print("Jogador 1, você venceu!")
#                 acertou = True
#             else:
#                 print(f"\nJogador 2, agora é sua última vez de tentar acertar a palavra. \nA primeira dica foi {dicas[iterador - 1]}. \nA segunda dica foi: {dicas[iterador]}.")
#                 print(f"E a terceira dica é {dicas[iterador]}.")
#                 chute4 = input("Tente acertar a palavra, Jogador 2!: ")
#                 if chute4 == palavra:
#                     print("Jogador 2, você venceu!")
#                     acertou = True
#                 else:
#                     iterador += 1
#                     print("O jogo acabou e nenhum dos dois venceu... Mais sorte na próxima!")


################# VERSÃO 2

import random

dicionario = {
    "machado": {
        "dica_1": "é um sobrenome",
        "dica_2": "corta madeira",
        "dica_3": "de assis"
    },
    "são paulo": {
        "dica_1": "nome de santo",
        "dica_2": "nome de cidade",
        "dica_3": "nome de time"
    },
    "planeta": {
        "dica_1": "o sol não é",
        "dica_2": "a lua não é",
        "dica_3": "a terra é"
    },
    "sanfona": {
        "dica_1": "instrumento musical",
        "dica_2": "fole",
        "dica_3": "luiz gonzaga"
    },
    "águia": {
        "dica_1": "ave com bico",
        "dica_2": "carnivora",
        "dica_3": "garras"
    },
    "alergia": {
        "dica_1": "poeira",
        "dica_2": "tinta",
        "dica_3": "doença"
    },
    "açúcar": {
        "dica_1": "cana",
        "dica_2": "beterraba",
        "dica_3": "cristais"
    },
    "áfrica": {
        "dica_1": "antigo continente",
        "dica_2": "deserto do saara",
        "dica_3": "leões e elefantes"
    },
    "adolescente": {
        "dica_1": "rebelde",
        "dica_2": "irresponsável",
        "dica_3": "quase adulto"
    },
    "aeroporto": {
        "dica_1": "pista",
        "dica_2": "hangar",
        "dica_3": "avião"
    },
    "agricultura": {
        "dica_1": "terra",
        "dica_2": "cultivo",
        "dica_3": "camponês"
    },
    "neblina": {
        "dica_1": "nevoeiro",
        "dica_2": "trevas",
        "dica_3": "nuvens"
    },
    "edifício": {
        "dica_1": "construção",
        "dica_2": "apartamentos",
        "dica_3": "arranha-céu"
    },
    "flauta": {
        "dica_1": "instrumento musical",
        "dica_2": "buracos",
        "dica_3": "sopro"
    }
}

palavra, dicas = random.choice(list(dicionario.items()))

print("Vamos começar nosso jogo, vocês receberão dicas para tentar acertar uma palavra!")
acertou = False
round = 1

##### FALTAM AJUSTES

#Depois trocar pra fazer algo que se assemelhe a um switch-case

while acertou == False and round <= 10:
    jogador1 = 1
    jogador2 = 2
    pontuacao1 = 0
    pontuacao2 = 0
    
    if round % 2 != 0:
        print(f"A primeira dica é: {dicas["dica_1"]}")
        chute1 = input(f"Jogador {jogador1}, tente acertar a palavra: ")
        if chute1 == palavra:
            print("Jogador 1, você venceu!")
            pontuacao1 += 5
            acertou = True
        else:
            print(f"\nJogador {jogador2}, agora é sua vez de tentar acertar a palavra. \nA segunda dica é {dicas["dica_02"]}..")
            chute2 = input("Qual seu chute?: ")
            if chute2 == palavra:
                print("Jogador 2, você venceu!")
                pontuacao2 += 3
                acertou = True
            else:
                print(f"\nJogador {jogador1}, agora é sua vez de tentar acertar a palavra. \nA terceira dica é {dicas["dica_03"]}")
                chute3 = input("Tente acertar a palavra, Jogador 1!: ")
                if chute3 == palavra:
                    print("Jogador 1, você venceu!")
                    pontuacao1 += 1
                    acertou = True
                else:
                    print("O jogo acabou e nenhum dos dois venceu... Mais sorte na próxima!")
    else:
        print(f"A primeira dica é: {dicas["dica_1"]}")
        chute1 = input(f"Jogador {jogador2}, tente acertar a palavra: ")
        if chute1 == palavra:
            print("Jogador 2, você venceu!")
            pontuacao2 += 5
            acertou = True
        else:
            print(f"\nJogador {jogador1}, agora é sua vez de tentar acertar a palavra. \nA segunda dica é {dicas["dica_02"]}.")
            chute2 = input("Qual seu chute?: ")
            if chute2 == palavra:
                print("Jogador 1, você venceu!")
                pontuacao1 += 3
                acertou = True
            else:
                print(f"\nJogador {jogador2}, agora é sua vez de tentar acertar a palavra. \nE a terceira dica é {dicas["dica_03"]}.")
                chute3 = input("Tente acertar a palavra, Jogador 2!: ")
                if chute3 == palavra:
                    print("Jogador 2, você venceu!")
                    pontuacao2 += 1
                    acertou = True
                else:
                    print("O jogo acabou e nenhum dos dois venceu... Mais sorte na próxima!")
    round += 1
    
    list(dicionario.items()).remove(palavra, dicas)
    #Ver se essa lógica pra remoção da palavra e dicas que já foram funciona de fato
    
    palavra, dicas = random.choice(list(dicionario.items()))
    
    
    
    

