import flet as ft

# 1 - Formulário de cadastro com validação

# def principal(page: ft.Page):
#     campo_nome = ft.TextField(label="Digite seu nome: ")
#     campo_email = ft.TextField(label="Digite seu email: ")
#     campo_idade = ft.TextField(label="Digite sua idade: ")

#     def validar(evento):
#         if not campo_nome.value or not campo_email.value or not campo_idade.value:
#             mensagem = ft.Text("Todos os campos devem ser preenchidos.")
#         elif int(campo_idade.value) < 0:
#             mensagem = ft.Text("Idade inválida.")
#         else:
#             mensagem = ft.Text("Cadastro feito com sucesso!")
#         page.add(mensagem)

#     enviar = ft.ElevatedButton("Enviar", on_click=validar)

#     page.add(campo_nome, campo_email, campo_idade, enviar)

# ft.app(target=principal)

# 2 - Contador Reverso >> Ao clickar no botão de contagem regressiva, o contador deverá começar a contar de 10 até 0 com intervalo de exibição de 1s entre cada número da sequência.

#TBC 
def principal(page: ft.Page):
    def iniciar_contagem(e):
        ...

    contagem_regressiva = ft.ElevatedButton("Iniciar Contagem Regressiva!", on_click=iniciar_contagem)

    page.add(contagem_regressiva)

ft.app(target=principal)