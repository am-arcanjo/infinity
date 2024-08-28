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

def verificar_caractere(texto: str, letra: chr):
    for chr in texto:
        if chr == letra:
            return True
    return False

print(verificar_caractere("lalalala", "b"))  
print(verificar_caractere("lalalala", "a"))  
