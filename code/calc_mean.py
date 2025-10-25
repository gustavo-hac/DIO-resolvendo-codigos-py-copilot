# Calcular a média de notas fornecidas na entrada do usuário a quantidade de notas é fornecida pelo usuário.
qtd_error = True
num_error = True
qtd = ""

qtd = input("Digite a quantidade de números para a média: ")
while not qtd.isdigit():
    print("\nERRO: A entrada precisa ser somente números\n")
    qtd = input("Digite a quantidade de números para a média: ")

qtd = int(qtd)
sum = 0.0
for i in range(qtd):
  while num_error:
    try:
      num = float(input(f"Digite o {i+1}° número: "))
      if num >= 0:
        num_error = False
        sum+=num
        i+=1
      else:
        print("\nErro: Digite apenas números positivos\n")
    except ValueError:
      print("\nErro: Digite apenas números\n")
  num_error = True

result = sum / qtd

print(f"A média é {result}.")