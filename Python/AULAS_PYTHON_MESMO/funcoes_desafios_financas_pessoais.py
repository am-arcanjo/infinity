# Desenvolver um sistema para gerenciar finanças pessoais;
# Categorias > utilizar um conjunto (set) para armazenar categorias
# Receitas > armazenar as receitas em uma lista de dicionários, onde cada dicionário contém uma descrição e um valor
# Despesas > armazenar as despesasem uma lista de dicionários, onde cada dicionário contém uma descrição, um valor e uma categoria
# Orçamentos > utilizar um dicionário para armazenar orçamentos, onde a chave é a categoria e o valor é o valor do orçamento 
# Sair

# PAUSEI PRA REFORMULAR O JOGO DE PISTAS / ONGOING
 

import re


isContinue = True
categorias_de_gastos = {}
receitas = {}
despesas = {}
orcamentos = {}

def continuar_selecao(): 
    selecao = int(input("\n Escolha o que quer fazer: \n 1. Adicionar Categoria de Gasto \n 2. Remover Categoria de Gasto \n 3. Listar Categorias de Gasto \n 4. Adicionar Receita \n 5. Registrar Compra \n 6. Ver Histórico de Compras \n 7. Mostrar Cliente Com Mais Compras \n 8. Mostrar Total de Clientes \n 9. Sair \n "))
    print(selecao)
    return selecao

def adicionar_categoria(categorias: str, categoria: str):
    categoria = {"Categoria de Gasto": categorias, "Categoria": categoria}
    categorias_de_gastos.append(categoria)

def remover_categoria(nome_categoria: str):
    ocorrencias = 0
    for categoria in categorias_de_gastos:
        if(categoria["Nome"] == nome_categoria):
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
    despesa = {"Descrição": descricao, "Valor": valor, "Categoria a qual pertence": nome_da_categoria}
    ocorrencias = 0    
    for categoria in categorias_de_gastos:
        if categoria["Categoria de Gastos"] == nome_da_categoria:
            despesas.append(despesa)
            ocorrencias += 1
    if ocorrencias == 0:
        print("A categoria para despesa apontada não existe.")        
    
def listar_receitas():       
    for receita in receitas:
        print("Descrição: " + receita["Descrição"] + "\n" + "Valor: " + receita["Valor"] + "\n") 

def listar_despesas():
    for despesa in despesas:
        print("Descrição: " + despesa["Descrição"] + "\n" + "Valor: " + despesa["Valor"] + "\n" "Categoria de gastos: " + despesa["Categoria a qual pertence"] + "\n") 

def listar_despesas_categoria(categoria: str):
    ocorrencias = 0
    for despesa in despesas:
        if despesa["Categoria a qual pertence"] == categoria:
            print("Descrição: " + despesa["Descrição"] + "\n" + "Valor: " + despesa["Valor"] + "\n" "Categoria de gastos: " + despesa["Categoria a qual pertence"] + "\n")
            ocorrencias += 1
    if ocorrencias == 0:
        print("Ou a categoria apontada não existe, ou não existem despesas nesta categoria")

#PAREI AQUI DE AJUSTAR

# def calcular_total_receitas():
#     for cliente in clientes:
#         print("Nome do cliente: " + cliente["Nome"] + "\n" + "E-mail do cliente: " + cliente["E-mail"] + "\n")

# def calcular_total_despesas():
#     for cliente in clientes():
#         print("Nome do cliente: " + cliente["Nome"] + "\n" + "E-mail do cliente: " + cliente["E-mail"] + "\n")

# def calcular_saldo_total():
#     for cliente in clientes:
#         print("Nome do cliente: " + cliente["Nome"] + "\n" + "E-mail do cliente: " + cliente["E-mail"] + "\n")

# def adicionar_orcamento():
#     cliente = {"Nome": nome, "E-mail": email, "Compras": []}
#     clientes.append(cliente)

# def listar_orcamentos():
#     for cliente in clientes:
#         print("Nome do cliente: " + cliente["Nome"] + "\n" + "E-mail do cliente: " + cliente["E-mail"] + "\n")

# def verificar_despesa_por_orcamento():
#     for cliente in clientes:
#         print("Nome do cliente: " + cliente["Nome"] + "\n" + "E-mail do cliente: " + cliente["E-mail"] + "\n")

# def limpar_financas():
#     global isContinue
#     isContinue = False
#     despesas = {}
#     receitas = {}
#     orcamentos = {}
#     print("Você limpou todo o histórico de finanças.")
#     return isContinue

# while isContinue:
#     selecao = continuar_selecao()

#     if selecao == 1:
#         nome_do_cliente = input("Indique o nome do cliente: ")
#         email_do_cliente = input("E o e-mail do cliente: ")
#         adicionar_cliente(nome_do_cliente, email_do_cliente)

#     elif selecao == 2:
#         nome_do_cliente = input("Indique o nome do cliente que deseja remover: ")
#         remover_cliente(nome_do_cliente)

#     elif selecao == 3:
#         nome_do_cliente = input("Indique o nome do cliente cujas informações deseja buscar: ")
#         buscar_cliente()

#     elif selecao == 4:
#         listar_clientes()

#     elif selecao == 5:
#         nome_do_cliente = input("Indique o nome do cliente cuja compra deseja cadastrar: ")
#         registrar_compras(nome_do_cliente)

#     elif selecao == 6:
#         nome_do_cliente = input("Indique o nome do cliente cujo histórico de compras queira ver: ")
#         ver_historico_compras(nome_do_cliente)

#     elif selecao == 7:
#         cliente_com_mais_compras()

#     elif selecao == 8:
#         total_clientes()

#     elif selecao == 9:
#         sair()