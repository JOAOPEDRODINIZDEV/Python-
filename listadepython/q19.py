total = int(input("Digite quantos numeros que você deseja digitar:"))
lista_numero = []

for j in range(total):
    nnumero = int(input("Digite os números: "))
    lista_numero.append(nnumero)
    
lista_numero.sort()
print("A ordem cresente dos são:",lista_numero)
    