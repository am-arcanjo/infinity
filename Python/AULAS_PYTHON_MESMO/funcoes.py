# Cada função tem de ter sua funcionalidade única, ou seja, fazer uma coisa só
# Funções são reutilizáveis, a partir do momento em que foi definida, ela pode ser chamada infinitas vezes
# Podem ou não receber parâmetros

# Os parâmetros de uma função só existem dentro do parêntese da função, ou seja, se eu quisesse passar uma variável qualquer para dentro da função, eu tenho que passar essa variável na chamada em si, que inclusive não precisa ter o mesmo nome do parâmetro
def boa_noite(nome: str):
    print(f"Boa noite, {nome}")

boa_noite("Arcanjo") 

def bom_dia(nome: str):
    print(f"Bom dia, {nome}")

nome_do_usuario = input("Digite seu nome: ")

bom_dia(nome_do_usuario)
