import contas

#Também teria como importar usando from tal que "from contas import somar, subtrair, dividir, multiplicar", e daí no resultado daria pra chamar direto as operações sem passar "contas."

a = int(input("Digite seu primeiro número: "))
b = int(input("Digite seu segundo número: "))
operacao = input("Digite a operação desejada (+, -, * ou /): ")

if operacao == "+":
    resultado = contas.somar(a, b)
elif operacao == "-":
    resultado = contas.subtrair(a, b)
elif operacao == "*":
    resultado = contas.multiplicar(a, b)
elif operacao == "/":
    resultado = contas.dividir(a, b)

print(resultado)