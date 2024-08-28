# Python Funções Exercícios de Aprendizagem

#  1 - Crie uma função chamada contar_caracteres que receba um parâmetro texto. A função deve retornar o número de caracteres na string.

# def contar_caracteres(texto: str):
#    return len(texto)

# print(contar_caracteres("alguém me dê uma neosaldina pelo amor de deus"))

# 2 - Crie uma função chamada repetir_string que receba dois parâmetros: texto e n. A função deve retornar a string exto repetida n vezes.

# def repetir_string(texto: str, n: int):
#     i = 0
#     while i <= n:
#         print(texto)
#         i += 1

# repetir_string("eco", 13)


# 3 - Crie uma função chamada verificar_caractere que receba dois parâmetros: texto e caractere. A função deve retornar True caso o caractere selecionado esteja presente na string texto, e False caso contrário.

# def verificar_caractere(texto: str, letra: chr):
#     for chr in texto:
#         if chr == letra:
#             return True
#     return False

# print(verificar_caractere("lalalala", "b"))  
# print(verificar_caractere("lalalala", "a"))  


# Funções Lambda
# É como se fosse uma função simplificada
# nomeDaFuncao = lambda parametro1, parametro2: parametro1 + parametro2
# Note que é possível fazer quaisquer operações com os parâmetros, não só soma
# Ainda: não é necessário declarar os tipos dos parâmetros, porém, é considerado melhor escrito colocando

# Exercícios Fixação
# 1 - Crie uma função que usa lambda para adicionar 10 a um determinado número dado

# soma_dez = lambda numero: numero + 10
# print(soma_dez(67))

# 2 - Crie uma função lambda para verfificar se o número inputado é maior do que 20

# maior_que_vinte = lambda numero: numero > 20
# print(maior_que_vinte(21))
# print(maior_que_vinte(14))

# 3 - Crie uma função lambda que multiplica um número dado por 3

# multiplica_por_3 = lambda numero: numero * 3
# print(multiplica_por_3(89))

# 4 - Crie uma função lambda que retorna o texto dado todo em letras maiúsculas

# letras_maiusculas = lambda texto: texto.upper()
# print(letras_maiusculas("pequenininhas"))

# 5 - Crie uma função lambda para subtrair 5 de um número dado

# subtrai_cinco = lambda numero: numero - 5
# print(subtrai_cinco(5))

# 6 - Crie uma função lambda para verificar se um número é positivo ou negativo

# positivo_ou_negativo = lambda numero: numero >= 0

# numero = int(input("Insira um número: "))
# if positivo_ou_negativo(numero):
#     print("Positivo")
# else:
#     print("Negativo")

# 7 - Crie uma função lambda que calcula a média de dois dados

# media = lambda numero1, numero2: ((numero1 + numero2) / 2)
# print(media(60, 44))

# 8 - Crie uma função lambda que substitua todas as ocorrências de um caractere 'a' por 'o' em uma string dada

substitui = lambda texto: texto.replace("a", "o")
print(substitui("Parca"))
