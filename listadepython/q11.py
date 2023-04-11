total = int(input("Digite quantos numeros que você deseja digitar:" ))
lista =[]
numeros_pares = []

for j in range(total):
    numeros = int(input("Digites os números: "))
    lista.append(numeros)
    if numeros %2 == 0:
        numeros_pares.append(numeros)
print("Os numeros pares são: ",numeros_pares)
    
   
   
    
    