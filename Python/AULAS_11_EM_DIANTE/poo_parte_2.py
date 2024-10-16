#A aula 11 eu não compareci, mas foi de POO, foi dado um basicão sobre o que é, o que significa na prática, etc

#Exercício: criar classe pessoa que tem atributos nome e idade, e um método apresentar que imprime esses atributos. Crie uma subclasse que herda de pessoa chamada Estudante, que tem além de nome e idade da classe superlativa, um atributo curso. Apresentar aqui deve também imprimir o curso. E crie mais uma subclasse chamada Professor, que também herda de Pessoa. Crie um método apresentar com uma string adequada.

import random

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

#Exercício 2: Crie uma classe chamada Animal que tenha um atributo nome. Adicione um método de fazer som que retorne o som do animal. Depois crie uma classe cachorro (ou outra) que sobrescreva o método de fazer som para retornar a onomatópeia deste animal. Crie um objeto do novo animal com o nome dele e imprima o som que ele faz.

class Animal:
    def __init__(self, nome):
        self.nome

class Raposa:
    def __init__(self, nome):
        super.__init__(nome)
        
    def fazer_som(nome):
        fox_sounds = ["Wa-pa-pa-pa-pa-pa-pow!", "Gering-ding-ding-ding-dingeringeding!", "Joff-tchoff-tchoffo-tchoffo-tchoff!", "Jacha-chacha-chacha-chow!", 
        "Fraka-kaka-kaka-kaka-kow!", 
        "A-hee-ahee ha-hee!",
        "A-oo-oo-oo-ooo!"]
        
        fox_sound = random.choice(fox_sounds)
        
        print(f"Esta é a raposa {nome}, e what does the fox say? {fox_sound}")

Raposa.fazer_som("Jackie")