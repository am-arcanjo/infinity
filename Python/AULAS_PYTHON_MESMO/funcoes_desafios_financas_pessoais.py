# Desenvolver um sistema para gerenciar finanças pessoais;
# Categorias > utilizar um conjunto (set) para armazenar categorias
# Receitas > armazenar as receitas em uma lista de dicionários, onde cada dicionário contém uma descrição e um valor
# Despesas > armazenar as despesasem uma lista de dicionários, onde cada dicionário contém uma descrição, um valor e uma categoria
# Orçamentos > utilizar um dicionário para armazenar orçamentos, onde a chave é a categoria e o valor é o valor do orçamento 
# Sair

# PAUSEI PRA REFORMULAR O JOGO DE PISTAS / ONGOING
 

import re


isContinue = True
categorias_de_gastos = []
receitas = []
despesas = []
orcamentos = {}

def continuar_selecao(): 
    selecao = int(input("\n Escolha o que quer fazer: \n 1. Adicionar Categoria de Gasto \n 2. Remover Categoria de Gasto \n 3. Listar Categorias de Gasto \n 4. Adicionar Receita \n 5. Adicionar Despesa \n 6. Listar Todas as Receitas \n 7. Listar Todas as Despesas \n 8. Listar Despesas por Categoria \n 9. Calcular Total de Receitas \n 10. Calcular Total de Despesas \n 11. Calcular o Saldo Total \n 12. Adicionar um Orçamento \n 13. Listar Orçamentos \n 14. Verificar Despesas por orçamento \n 15. Limpar Finanças \n \n"))
    print(selecao)
    return selecao

def adicionar_categoria(categorias: str, categoria: str):
    categoria = {"Categoria de Gasto": categorias, "Categoria": categoria}
    categorias_de_gastos.append(categoria)

def remover_categoria(nome_categoria: str):
    ocorrencias = 0
    for categoria in categorias_de_gastos:
        if(categoria["Categoria"] == nome_categoria):
            categorias_de_gastos.remove(categoria)
            ocorrencias += 1
    if ocorrencias == 0:
        print("Esta categoria não existe, então não é possível remover a mesma.")
    
def listar_categorias():
    for categoria in categorias_de_gastos:
        print("Nome da Categoria de Gastos: " + categoria["Categoria de Gasto"] + "\n" + "Categoria: " + categoria["Categoria"] + "\n")

def adicionar_receita(descricao: str, valor: int):  
    receita = {"Descrição": descricao, "Valor": valor}
    receitas.append(receita)

def adicionar_despesa(descricao: str, valor: int, nome_da_categoria: str):
    despesa = {"Descrição": descricao, "Valor": valor, "Categoria de Gasto": nome_da_categoria}
    ocorrencias = 0    
    for categoria in categorias_de_gastos:
        if categoria["Categoria de Gasto"] == nome_da_categoria:
            despesas.append(despesa)
            ocorrencias += 1
    if ocorrencias == 0:
        print("A categoria para despesa apontada não existe.")        
    
def listar_receitas():       
    for receita in receitas:
        print("Descrição: " + receita["Descrição"] + "\n" + "Valor: " + receita["Valor"] + "\n") 

def listar_despesas():
    for despesa in despesas:
        print("Descrição: " + despesa["Descrição"] + "\n" + "Valor: " + str(despesa["Valor"]) + "\n" "Categoria de gastos: " + despesa["Categoria a qual pertence"] + "\n") 

def listar_despesas_categoria(categoria: str):
    ocorrencias = 0
    for despesa in despesas:
        if despesa["Categoria a qual pertence"] == categoria:
            print("Descrição: " + despesa["Descrição"] + "\n" + "Valor: " + str(despesa["Valor"] + "\n" "Categoria de gastos: " + despesa["Categoria a qual pertence"] + "\n"))
            ocorrencias += 1
    if ocorrencias == 0:
        print("Ou a categoria apontada não existe, ou não existem despesas nesta categoria")

def calcular_total_receitas():
    total = 0
    for receita in receitas:
        total += receita["Valor"]
    print("Seu total de receitas é: " + str(total))    

def calcular_total_despesas():
    total = 0
    for despesa in despesas:
        total += despesa["Valor"]
    print("Seu total de despesas é: " + str(total))

def calcular_saldo_total():
    total_despesas = calcular_total_despesas()
    total_receitas = calcular_total_receitas()
    final = total_receitas - total_despesas

    print("Seu saldo total é: " + final)

def adicionar_orcamento(categoria: str, valor: str):
    categoria = {"Categoria": categoria, "Orçamento": valor}
    categorias_de_gasto.append(categoria)

def listar_orcamentos():
    for categoria in categorias_de_gasto:
        print("Categoria: " + categoria["Categoria"] + "\n" + "Orçamento" + categoria["Orçamento"] + "\n")
   
def verificar_despesa_por_orcamento():
    categoria = {"Saldo Disponível": categoria["Orçamento"] - categoria["Despesa"]}
    for categoria in categorias_de_gasto:
        print("Categoria" + categoria["Categoria"] + "\n" + "Orçamento: " + categoria["Orçamento"] + "\n" + "Valor restante após gastos: " + categoria["Saldo Disponível"])
   
def limpar_financas():
    global isContinue
    isContinue = False
    despesas = {}
    receitas = {}
    orcamentos = {}
    print("Você limpou todo o histórico de finanças.")
    return isContinue

while isContinue:
    selecao = continuar_selecao()

    if selecao == 1:
        categorias = input("Indique a categoria de gastos: ")
        categoria = input("Indique o nome da nova categoria: ")
        adicionar_categoria(categorias, categoria)

    elif selecao == 2:
        categoria = input("Indique o nome da categoria que deseja remover: ")
        remover_categoria(categoria)

    elif selecao == 3:
        listar_categorias()

    elif selecao == 4:
        descricao = input("Adicione uma descrição à sua receita: ")
        valor = int(input("Indique o valor: "))

        adicionar_receita(descricao, valor)

    elif selecao == 5:
        descricao = input("Adicione uma descrição à sua receita: ")
        valor = int(input("Indique o valor: "))
        nome_da_categoria = input("Indique a categoria a qual essa despesa pertence: ")

        adicionar_despesa(descricao, valor, nome_da_categoria)

    elif selecao == 6:
        listar_receitas()

    elif selecao == 7:
        listar_despesas()

    elif selecao == 8:
        categoria = input("Indique o nome da categoria a qual deseja consultar as despesas: ")

        listar_despesas_categoria()

    elif selecao == 9:
        calcular_total_receitas()

    elif selecao == 10:
        calcular_total_despesas()

    elif selecao == 11:
        calcular_saldo_total()

    elif selecao == 12:
        categoria = input("Indique a categoria na qual deseja adicionar um orçamento: ")
        valor = int(input("Indique o valor do orçamento: "))

    elif selecao == 13:
        listar_orcamentos()

    elif selecao == 14:                          
        verificar_despesas_por_orcamento()

    elif selecao == 15:
        limpar_financas()