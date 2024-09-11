# Clássico jogo do Sílvio Santos das 3 pistas. A ideia é que o usuário adivinhe uma palavra em 3 tentativas, e a cada tentativa errada, seja fornecida uma dica. Se ele exaurir as dicas, e mesmo assim não acertar, ele perde.
# O professor reformulou tal que a ideia é competir com um segundo jogador.
# O jogador 1 receberá a primeira dica e tentará acertar. Caso não acerte, o jogo irá para o jogador 2 que tentará acertar após receber a segunda dica (e saber a primeira). Após isso, caso ainda não acerte, o jogador 1 receberá a terceira dica e tentará acertar. Se não der certo, o joador 2 tenta com todas as três dicas. Se nem assim for, ambos perdem.

import random

dicionario = {
    "machado": {
        1: "é um sobrenome",
        2: "corta madeira",
        3: "de assis"
    },
    "são paulo": {
        1: "nome de santo",
        2: "nome de cidade",
        3: "nome de time"
    },
    "planeta": {
        1: "o sol não é",
        2: "a lua não é",
        3: "a terra é"
    },
    "sanfona": {
        1: "instrumento musical",
        2: "fole",
        3: "luiz gonzaga"
    },
    "águia": {
        1: "ave com bico",
        2: "carnivora",
        3: "garras"
    },
    "alergia": {
        1: "poeira",
        2: "tinta",
        3: "doença"
    },
    "açúcar": {
        1: "cana",
        2: "beterraba",
        3: "cristais"
    },
    "áfrica": {
        1: "antigo continente",
        2: "deserto do saara",
        3: "leões e elefantes"
    },
    "adolescente": {
        1: "rebelde",
        2: "irresponsável",
        3: "quase adulto"
    },
    "aeroporto": {
        1: "pista",
        2: "hangar",
        3: "avião"
    },
    "agricultura": {
        1: "terra",
        2: "cultivo",
        3: "camponês"
    },
    "neblina": {
        1: "nevoeiro",
        2: "trevas",
        3: "nuvens"
    },
    "edifício": {
        1: "construção",
        2: "apartamentos",
        3: "arranha-céu"
    },
    "flauta": {
        1: "instrumento musical",
        2: "buracos",
        3: "sopro"
    }
}

palavra, dicas = random.choice(list(dicionario.items()))

print("Vamos começar nosso jogo, vocês receberão dicas para tentar acertar uma palavra!")
acertou = False
iterador = 1

while acertou == False and iterador <= 3:
    print(f"A primeira dica é: {dicas[iterador]}")
    chute1 = input("Jogador 1, tente acertar a palavra: ")
    if chute1 == palavra:
        print("Jogador 1, você venceu!")
        acertou = True
    else:
        print(f"\nJogador 2, agora é sua vez de tentar acertar a palavra. \nA primeira dica foi: {dicas[iterador]}.")
        iterador += 1 
        print(f"E a segunda dica é {dicas[iterador]}.")
        chute2 = input("Qual seu chute?: ")
        if chute2 == palavra:
            print("Jogador 2, você venceu!")
            acertou = True
        else:
            print(f"\nJogador 1, agora é sua vez de tentar acertar a palavra. \nA primeira dica foi {dicas[iterador - 1]}. \nA segunda dica foi: {dicas[iterador]}.")
            iterador += 1
            print(f"E a terceira dica é {dicas[iterador]}.")
            chute3 = input("Tente acertar a palavra, Jogador 1!: ")
            if chute3 == palavra:
                print("Jogador 1, você venceu!")
                acertou = True
            else:
                print(f"\nJogador 2, agora é sua última vez de tentar acertar a palavra. \nA primeira dica foi {dicas[iterador - 1]}. \nA segunda dica foi: {dicas[iterador]}.")
                print(f"E a terceira dica é {dicas[iterador]}.")
                chute4 = input("Tente acertar a palavra, Jogador 2!: ")
                if chute4 == palavra:
                    print("Jogador 2, você venceu!")
                    acertou = True
                else:
                    iterador += 1
                    print("O jogo acabou e nenhum dos dois venceu... Mais sorte na próxima!")




