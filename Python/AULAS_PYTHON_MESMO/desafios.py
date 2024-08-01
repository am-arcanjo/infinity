# São 5 desafios, mas não será possível fazer todos na mesma aula
# 1 - Vocês devem criar um jogo da memória simples. Terá uma lista de palavras e e o jogar precisa adivinhar onde estão as palavras repetidas.
# import random

# pergunta1 = int(input("Escolha uma posição da lista (lembrando que a lista inicia-se pelo 0 e temos 10 valores inicialmente): "))
# pergunta2 = int(input("Escolha outra posição da lista para ver se você encontrou o par: "))

# jogoTerminou = False

# palavras = ["gato", "gato", "cachorro", "cachorro", "pássaro", "pássaro", "cavalo", "cavalo", "boi", "boi"]

# #random.shuffle(palavras)

# while (jogoTerminou == False):
#     if(pergunta2 == pergunta1):
#         print('Tentando roubar? Coloque índices diferentes!')
#         jogoTerminou = True

#     elif (palavras[pergunta1] == palavras[pergunta2]):
#         print('Você acertou uma dupla, continue!')
#         palavras = list(filter(lambda p: p != palavras[pergunta1], palavras))

#         pergunta1 = int(input('Escolha uma posição da lista (lembrando que a lista inicia-se pelo 0 e retiramos o(s) par(es) encontrado(s)): '))
#         pergunta2 = int(input("Escolha outra posição da lista para ver se você encontrou o próximo par: "))

#         if(len(palavras) == 0):
#             print('Parabéns, você ganhou!')
#             jogoTerminou = True

#     elif (palavras[pergunta1] != palavras[pergunta2]):
#         print('Você não conseguiu, mais sorte da próxima vez')
#         jogoTerminou = True

# 2- Vocês devem criar um jogo de adivinhação onde o jogador precisa adivinhar um número escolhido aleatoriamente de uma tupla de números. O jogo dá dicas se o número é maior ou menor do que o palpite.

numero = 10

palpite = 0

while palpite != numero:
    palpite = int(input("Tente acertar o número: "))
    if (palpite == numero):
        print('Parabéns! Você acertou');
        break

