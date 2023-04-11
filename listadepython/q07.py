total = int(input("Quatas frases que você deseja digita: "))
maoir_palavra = ""

for j in range(total):
    frase = input("Qual é a frase:")
if len(frase) > len(maoir_palavra):
    maoir_palavra = frase
print("A maior frase é:",maoir_palavra) 

