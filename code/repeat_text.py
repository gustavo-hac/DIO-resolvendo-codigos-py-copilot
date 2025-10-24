# Progama que solicita duas entradas: um texto e um número inteiro positivo definindo quantas vezes a palavra será repetida.
text = input("Digite o texto: ")
times = input("Digite o número de repetições: ")
while not times.isdigit():
  print("ERRO: Número precisa ser um inteiro positivo")
  times = input("Digite o número de repetições: ")

times = int(times)
if(times == 0):
  print("Sem texto pra você então: \n")
else:
  text_concat = (text + " ") * int(times)
  print("Texto repetido " + str(times) + " vezes:\n" + text_concat)