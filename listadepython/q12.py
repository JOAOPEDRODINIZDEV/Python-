total = int(input("Digite quantos numeros que você deseja digitar:" ))
lista =[]
numeros_impares = []

for j in range(total):
    numeros = int(input("Digites os números: "))
    lista.append(numeros)
    if numeros %2 != 0:
        numeros_impares.append(numeros)
print("Os numeros impares são: ",numeros_impares)