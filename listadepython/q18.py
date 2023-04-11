total = int(input("Digite quantos numeros você deseja digitar: "))
lista = []
produto = 1

for i in range(total):
    numeros = int(input("Digite os números: "))
    lista.append(numeros)
    produto *= numeros
print("O resultado da media é: ",produto)
    
    