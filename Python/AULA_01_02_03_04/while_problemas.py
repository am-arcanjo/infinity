#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

#while True:
#    nota = int(input('Gentileza, digitar uma nota entre 0 e 10: '))
    
#    if nota < 0 or nota > 10:
#        print('A nota digitada é inválida.')
#    else:
#       break

#print(f'A nota digitada é: {nota}')

#Crie um programa que leia o estado civil de uma pessoa. Seu programa deverá aceitar somente os valores abaixo. Caso o valor digitado seja inválido, pergunte novamente.

while True:
    estado_civil = input('Gentileza, informar seu estado civil (s/c/v/d): ')
    
    if estado_civil != 's' and estado_civil != 'c' and estado_civil != 'd' and estado_civil != 'v': 
        print('O estado civil digitado não é válido.')
    elif estado_civil == 's' :
        print('Você é solteiro.')
        break
    elif estado_civil == 'c' :
        print('Você é casado.')
        break
    elif estado_civil == 'v' :
        print('Você é viúvo.')
        break
    elif estado_civil == 'd' :
        print('Você é divorciado.')
        break


