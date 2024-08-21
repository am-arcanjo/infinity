# 1 - Crie uma função chamada area_retangulo que receba dois parâmetros: largura e altura. A função deve retornar a área do retângulo, que é calculada como largura * altura.

# def area_retangulo(largura: int, altura: int):
#     print(largura * altura)

# area_retangulo(4, 30)



# 2 - Crie uma função chamada dividir que receba dois parâmetros: a e b. A função deve retornar a divisão de a e b.

# def dividir(a: int, b: int):
#     print(a/b)

# dividir(3414, 78251)



# 3 - Crie uma função chamada eh_positivo que receba um parâmetro numero. A função deve retornar True se o número for positivo e False se não for.

# def eh_positivo(numero: int): 
#     if numero >= 0:
#         print("Seu número é positivo!")
#     else:
#         print("Seu número é negativo!")

# numero_escolhido = int(input("Digite um número para averiguar se ele é negativo ou positivo: "))

# eh_positivo(numero_escolhido)



# 4 - Crie uma função chamada quadrado que receba um parâmetro numero. A função deve retornar o quadrado de numero.

# def quadrado(numero: int):
#     print(numero * numero)

# quadrado(144)



# 5 - Crie uma função chamada string_vazia que receba um parâmetro texto. A função deve retornar True se a string estiver vazia e False caso contrário.

# def string_vazia(texto: str):
#     if texto == "":
#         print(True)
#     else:
#         print(False)

# textoQualquer = input("Digite algo e te diremos se está vazio (verdadeiro) ou não: ")
# string_vazia(textoQualquer)



# 6 - Crie uma função chamada celsius_para_fahrenheit que receba um parâmetro celsius.
# A função deve retornar a temperatura em Fahrenheit, calculada pela fórmula fahrenheit = (celsius * 9/5) + 32.

def celsius_para_farenheit(celsius: float):
    print((celsius * 9/5) + 32)

celsius_para_farenheit(-40)
# Fun fact: -40 é a única temperatura onde tanto em Farenheit quanto em Celsius temos o mesmo valor.