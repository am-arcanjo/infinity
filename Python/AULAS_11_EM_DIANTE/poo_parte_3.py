# Exercícios da parte 3

# Associação entre médico e paciente: crie uma classe médico e uma classe paciente. O Paciente deve ter um nome e uma lista de consultas, enquanto o Médico deve ter um método para marcar consulta com um paciente. A consulta deve ser registrada na lista de consultas do paciente e conter o nome do médico e data em que foi realizada.

class Paciente:
    def __init__(self, nome):
        self.nome = nome

class Medico:
    def __init__(self, nome, lista_consultas):
        self.nome = nome
        self.lista_consultas = lista_consultas
    
    def marcar_consulta(self, paciente:  Paciente, data):
        self.lista_consultas.append("Paciente: " + str(paciente.nome) + ", consulta realizada na data: " + data + ", e com o médico: " + self.nome)

    def listar_consultas_geral(self):
        for consulta in self.lista_consultas:
             print(consulta)

medico_1 = Medico("João", [])
paciente_1 = Paciente("Carlos")


medico_1.marcar_consulta(paciente_1, "20092015")
medico_1.listar_consultas_geral()


# Sobre encapsulamento e getters e setters
# No python podemos usar os clássicos métodos get_coisa e set_coisa ou podemos usar annotations @property pro getter e @coisa.setter pro setter
# Definimos o atributo que queremos que seja privado com __ antes do nome dele ou seja, self.coisa + __coisa; e dessa forma não é possível acessar e nem modificar o valor diretamente (sem os getters e setters).

# Exercício: Crie uma classe ContaBancaria que tenha saldo privado, e faça métodos para depositar, sacar e verificar o saldo

class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def modificar_saldo(self, valor):
        self.__saldo += valor
        
    def sacar(self, valor):
        modificar_saldo()
        

        
        
