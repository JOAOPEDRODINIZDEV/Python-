total = int(input("Digite quantos numeros você deseja digitar: "))
lista = []

for j in range(total):
    numero = int(input("Qual é o número: "))
    if not lista or numero < min(lista):
        lista.append(numero)

print("O menor número é ", min(lista))
