numeroDeAlunos = int(input('Por favor informe a quantidade de alunos: '))
alunosENotas = []
iterador = 0
notas = 0

while iterador < numeroDeAlunos:
    alunoENotas = []

    aluno = input('Digite o nome do aluno: ')
    alunoENotas.append(aluno)

    notas = 0
    while notas < 3:
        nota = int(input('Digite a nota do aluno: '))
        alunoENotas.append(nota)
        notas += 1

    iterador += 1
    alunosENotas.append(alunoENotas)

for aluno in alunosENotas:
    nomeAluno = aluno[0]
    notasAluno = aluno[1:]
    media = sum(notasAluno) / len(notasAluno)
    aprovado = ""
    if(media >= 7):
        aprovado = "Aprovado"
    else:
        aprovado = "Não aprovado."

    print(f'Aluno: {nomeAluno} | Média das notas: {media:.2f} | {aprovado}')

