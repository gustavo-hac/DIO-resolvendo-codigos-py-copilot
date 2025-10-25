# Programa para verificar se uma frase é um palíndromo. (ignora espaços)

palavra = input("Digite uma palavra: ")

palavra = palavra.replace(" ", "").lower()

if palavra == palavra[::-1]:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")