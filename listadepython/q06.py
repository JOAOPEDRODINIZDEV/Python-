total = int(input("Quantos numeros que você deseja digita: "))
lista =[]

for j in range(total):
    numero = int(input("Digite os numeros: "))
    lista = lista + [numero]
    soma = sum(lista)
print("Soam dos numeros são: ",soma)
    