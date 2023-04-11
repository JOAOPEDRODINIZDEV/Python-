total = int(input("Digite quantos numeros que você deseja digitar:"))
lista =[]

for j in range(total):
    numero = int(input("Qual é o número: "))
    lista.append(numero)
    soma = sum(lista)
    media = soma / len(lista)
print("A media dos números são: ",media)