# Teremos uma lista de tarefas que deverá ter as seguintes opções:
# Adicionar, Listar, Marcar como Concluída, Remover


selecao = int(input("Escolha o que quer fazer: \n 1. Adicionar Tarefa \n 2. Listar Tarefas \n 3. Marcar Tarefa como Concluída \n 4. Remover Tarefa \n 5. Sair \n"))

tarefas = []

def adicionar_tarefa(descricao: str):
    tarefa = {"descricao": descricao, "status": "pendente"}
    tarefas.append(tarefa)

def listar_tarefas():
    for i, tarefa in enumerate(tarefas):
        print(tarefa(i))

def marcar_conclusao(indice: int):
    tarefas[indice].status == "concluida"


def remover_tarefa(indice: int):
    tarefas.pop(indice)


if selecao == 1:
    descricao_da_tarefa = input("Escolha uma descrição para sua tarefa: ")
    adicionar_tarefa(descricao_da_tarefa)

elif selecao == 2:
    listar_tarefas

elif selecao == 3:
    indice_conclusao = input("Digite o índice da tarefa que deseja marcar como concluída (começa por 0): ")
    marcar_conclusao(indice_conclusao)

elif selecao == 4:
    indice_remocao = input("Digite o índice da tarefa que deseja remover(começa por 0): ")
    remover_tarefa(indice_remocao)

elif selecao == 5:
    print("Você saiu")
