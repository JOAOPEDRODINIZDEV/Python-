total = int(input("Digite quantos números que você dseja digitar: "))
lista = []
numeros_menores = []

for j in range(total):
    numeros = int(input("Digite os números: "))
    lista.append(numeros)
    if numeros < 5:
        numeros_menores.append(numeros)
if len(numeros_menores) > 0:
    print("Os nuúmeros menores que 5 são: ",numeros_menores) 
else:
    print("Nenhum dos numeros que voce digitou são menores do 5")
