lista_palavras = input("Digite uma lista de palavras separadas por espaço: ").split()
palavras_com_a = []

for palavra in lista_palavras:
    if palavra.startswith('a') or palavra.startswith('A'):
        palavras_com_a.append(palavra)

print("Palavras que começam com a letra 'a': ", palavras_com_a)