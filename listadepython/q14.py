total = int(input("Digite quantos números que você deeja digitar: "))
lista = []
numeros_acima = []

for j in range(total):
    numeros = int(input("Digite os números: "))
    lista.append(numeros)
    if numeros > 10:
        numeros_acima.append(numeros)
if len(numeros_acima) > 0:
    print("Os números acima que 10 são: ",numeros_acima) 
else:
    print("Nenhum dos números que voce digitou é acima do 10")
