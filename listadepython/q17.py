total = int(input("Digite quantos numeros  que você deseja digitar :"))
lista = []
numeros_impares = []

for j in range(total):
    numeros = int(input("Digite os Numeros: "))
    lista.append(numeros)
    if numeros %2 !=0:
       numeros_impares.append(numeros)
       soma = sum(numeros_impares)
       media = soma / len(numeros_impares)
print("A media dos numeros imapares são: ",media)