#Faça um programa que peça ao usuário o tempo em anos do carro dele. Se o carro tiver mais de 3 anos, imprima informando que é um carro velho, se não, imprima que é novo.

idade_carro = int(input('Quantos anos tem seu carro? '))

if (idade_carro > 3):
    print('Seu carro é velho.')
else:
    print('Seu carro é novo.')
