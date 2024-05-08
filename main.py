portatilA = [0, 1, 1]
portatilB = [1, 1, 1]
portatilC = [1, 0, 1]
portatilD = [1, 0, 0]
portatilE = [1, 1, 0]
portatilF = [0, 1, 0]

database = [portatilA, portatilB, portatilC, portatilD, portatilE, portatilF] # Dados
rotulo = ['Smartphone', 'Smartphone', 'Smartphone', 'Tablet', 'Tablet', 'Tablet'] # Respostas

dados = []


for x in range(2):
    
    android = int(input("digite um numero: "))
    if (android > 1):
        continue
         fortnite = int(input("digite um numero: "))
           bolso = int(input("digite um numero: "))

    dado = [android, fortnite, bolso]
    
    dados.append(dado)

    y_pred = modelo.predict(portateisDesconhecidos) # Cria as respostas para cada um dos portateis fornecidos


print('Resultados esperados: ')
print(y_pred)
print('Resultados obtidos:')
print(y_true)