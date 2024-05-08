portatilA = [0, 1, 1]
portatilB = [1, 1, 1]
portatilC = [1, 0, 1]
portatilD = [1, 0, 0]
portatilE = [1, 1, 0]
portatilF = [0, 1, 0]

database = [portatilA, portatilB, portatilC, portatilD, portatilE, portatilF] # Dados
rotulo = ['Smartphone', 'Smartphone', 'Smartphone', 'Tablet', 'Tablet', 'Tablet'] # Respostas

from sklearn.dummy import DummyClassifier # Biblioteca para Machine Learning

modelo = DummyClassifier() # Gera o modelo
modelo.fit(database, rotulo) # Faz com que o algoritmo aprenda sobre os dados que temos
# Iremos passar a base dados e nossas repostas

dados = []

for x in range(2):
    android = int(input("Digite um número: "))

    if (android > 1):
        continue

    fortnite = int(input("Digite um número: "))
    bolso = int(input("Digite um número: "))

    dado = [android, fortnite, bolso]

    dados.append(dado)

y_pred = modelo.predict(dados)

print('Resultados esperados: ')
print(y_pred)