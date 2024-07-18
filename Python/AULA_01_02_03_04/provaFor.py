inicio = int(input('Por gentileza, insira o início do intervalo: '))
fim = int(input('Por gentileza, insira o final do intervalo: '))

listaPares = []
total = 0

while inicio <= fim:
    if (int(inicio) % 2 == 0):
        listaPares.append(inicio)
    inicio += 1

for par in listaPares:
    total += par

print(total)