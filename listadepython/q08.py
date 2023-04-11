total = int(input("Digite quantos numeros que você deseja digitar: "))
lista = []

for j in range(total):
    numero = int(input("Qual é o número: "))
    if not lista or numero > max(lista):
        lista.append(numero)

print("O maior número é ", max(lista))
