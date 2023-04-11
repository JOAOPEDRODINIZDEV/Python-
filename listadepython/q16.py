total = int(input("Digite quantos numeros que você deseja digitar :"))
lista = []
numeros_pares = []

for j in range(total):
    numeros = int(input("Digite os Numeros: "))
    lista.append(numeros)
    if numeros %2 == 0:
       numeros_pares.append(numeros)
       soma = sum(numeros_pares)
       media = soma / len(numeros_pares)
print("A media dos números pares são: ",media)