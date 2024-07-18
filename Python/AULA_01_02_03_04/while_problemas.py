#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

#while True:
#    nota = int(input('Gentileza, digitar uma nota entre 0 e 10: '))
    
#    if nota < 0 or nota > 10:
#        print('A nota digitada é inválida.')
#    else:
#       break

#print(f'A nota digitada é: {nota}')

#Crie um programa que leia o estado civil de uma pessoa. Seu programa deverá aceitar somente os valores abaixo. Caso o valor digitado seja inválido, pergunte novamente.

# while True:
#     estado_civil = input('Gentileza, informar seu estado civil (s/c/v/d): ')
    
#     if estado_civil != 's' and estado_civil != 'c' and estado_civil != 'd' and estado_civil != 'v': 
#         print('O estado civil digitado não é válido.')
#     elif estado_civil == 's' :
#         print('Você é solteiro.')
#         break
#     elif estado_civil == 'c' :
#         print('Você é casado.')
#         break
#     elif estado_civil == 'v' :
#         print('Você é viúvo.')
#         break
#     elif estado_civil == 'd' :
#         print('Você é divorciado.')
#         break

#Peça ao usuário para digitar um número e exiba a tabuada desse número de 1 a 10.

# numero = int(input("Informe um número para saber sua tabuada: "))
# iterador = 1

# while iterador < 11:
#     print(numero * iterador)
#     iterador += 1

#Implemente um programa que solicite ao usuário que digite um nome de usuário e uma senha. O programa só deve permitir o acesso quando o usuário digitar corretamente um nome de usuário e senha predefinidos. Caso contrário, deve continuar solicitando até que o usuário entre com as informações corretas.

# nomeUsuario = 'generico'
# senhaUsuario = '1234'

# while True:
#     nomeTentativa = input('Digite o username: ')
#     senhaTentiva = input('Digite a senha: ')
#     if (nomeTentativa == nomeUsuario and senhaTentiva == senhaUsuario):
#         print('Correto, login feito.')
#         break
#     else:
#         print("Incorreto, tente novamente.")

#Solicite que o usuário digite números inteiros positivos e exiba a soma desses números. Encerre o programa quando o usuário digitar um número negativo.

soma = 0

while True:
    numero = int(input('Digite um número positivo (ou digite um número negativo para sair): '))
    if numero >= 0:
        soma += numero
    else:
        print('Sua soma é: ' + str(soma))
        break