#A aula 11 eu não compareci, mas foi de POO, foi dado um basicão sobre o que é, o que significa na prática, etc

#Exercício: criar classe pessoa que tem atributos nome e idade, e um método apresentar que imprime esses atributos. Crie uma subclasse que herda de pessoa chamada Estudante, que tem além de nome e idade da classe superlativa, um atributo curso. Apresentar aqui deve também imprimir o curso. E crie mais uma subclasse chamada Professor, que também herda de Pessoa. Crie um método apresentar com uma string adequada.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Estudante(Pessoa):
    def __init__(self, nome, idade, turma):
        super.__init__(nome, idade)
        self.turma = turma
    
    def apresentar(nome, idade, turma):
        print(f"Olá, eu sou o aluno {nome}, tenho {idade} anos e estou na turma {turma}.")

class Professor(Pessoa):
    def __init__(self, nome, idade):
        super.__init__(nome, idade)
    
    def apresentar(nome, idade):
        print(f"Olá, eu sou o professor {nome}, e tenho {idade} anos.")
        
Estudante.apresentar("Rico", 34, "Biologia Molecular")
Professor.apresentar("Gaspar", 51)