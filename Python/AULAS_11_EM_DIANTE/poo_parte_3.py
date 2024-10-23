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




        
        
