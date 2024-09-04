# Desenvolver um sistema de gerenciamento de clientes em Python com as seguintes operações:
# Adicionar cliente passando um nome e um email
# Remover um cliente utilizando seu nome
# Buscar um cliente pelo nome e exibir seu nome e email
# Listar clientes, exibindo todos os clientes cadastrados com seus nomes e emails
# Registrar a compra utilizando o nome do cliente e registrando sua compra
# Mostrar cliente com mais compras
# Sair

isContinue = True
clientes = []

def continuar_selecao(): 
    selecao = int(input("\n Escolha o que quer fazer: \n 1. Adicionar Cliente \n 2. Remover Cliente \n 3. Buscar Cliente \n 4. Listar Clientes \n 5. Registrar Compra \n 6. Ver Histórico de Compras \n 7. Mostrar Cliente Com Mais Compras \n 8. Mostrar Total de Clientes \n 9. Sair \n "))
    print(selecao)
    return selecao

def adicionar_cliente(nome: str, email: str):
    compras = []
    cliente = {"Nome": nome, "E-mail": email, "Compras": compras}
    clientes.append(cliente)

def remover_cliente(nome: str):
    ocorrencias = 0
    for cliente in clientes:
        if(cliente.nome == nome):
            clientes.pop(cliente)
            ocorrencias += 1
    if ocorrencias == 0:
        print("O cliente não existe, então não é possível remover o mesmo.")
    

def buscar_cliente(nome: str):
    ocorrencias = 0
    for cliente in clientes:
        if(cliente.nome == nome):
            print(cliente)
            ocorrencias += 1
    if ocorrencias == 0:
        print("Não existe cliente com o nome inserido.")

def listar_clientes():
    for cliente in clientes:
        print(cliente.nome)
        print(cliente.email)

def registrar_compras(nome: str):
    ocorrencias = 0
    for cliente in clientes:
        if(cliente.nome == nome):
            compra = input("Qual foi o produto adquirido pelo cliente? ")
            cliente.compras.append(compra)
            ocorrencias += 1
    if ocorrencias == 0:
        print("Não existe cliente com o nome inserido.")

def ver_historico_compras(nome: str):
    ocorrencias = 0
    for cliente in clientes:
        if cliente.nome == nome and cliente.compras.length != 0:
            print(cliente.compras)
        elif cliente.nome == nome and cliente.compras.length == 0:
            print("Este cliente não comprou nada ainda.")
    if ocorrencias == 0:
        print("Não existe cliente com o nome inserido.")        

def cliente_com_mais_compras(nome = "", email = "", compras = 0):
    cliente_mais_compras = {"Nome": nome, "E-mail": email,"Compras": compras}
    for cliente in clientes:
        if cliente.compras.length > cliente_mais_compras.compras:
            cliente_mais_compras.compras = cliente.compras
            cliente_mais_compras.nome = cliente.nome
            cliente_mais_compras.email = cliente.email
    print("Nome do cliente: " + cliente_mais_compras.nome + "\n" + "E-mail do cliente: " + cliente_mais_compras.email)        

def total_clientes():
    print(clientes.length)

def sair():
    isContinue = False
    clientes = []
    print("Você saiu.")
    return isContinue

while isContinue:
    selecao = continuar_selecao()

    if selecao == 1:
        nome_do_cliente = input("Indique o nome do cliente: ")
        email_do_cliente = input("E o e-mail do cliente: ")
        adicionar_cliente(nome_do_cliente, email_do_cliente)

    elif selecao == 2:
        nome_do_cliente = input("Indique o nome do cliente que deseja remover: ")
        remover_cliente(nome_do_cliente)

    elif selecao == 3:
        nome_do_cliente = input("Indique o nome do cliente cujas informações deseja buscar: ")
        buscar_cliente()

    elif selecao == 4:
        listar_clientes()

    elif selecao == 5:
        nome_do_cliente = input("Indique o nome do cliente cuja compra deseja cadastrar: : ")
        registrar_compras(nome_do_cliente)

    elif selecao == 6:
        nome_do_cliente = input("Indique o nome do cliente cujo histórico de compras queira ver: ")
        ver_historico_compras(nome_do_cliente)

    elif selecao == 7:
        cliente_com_mais_compras()

    elif selecao == 8:
        total_clientes()

    elif selecao == 9:
        sair()

