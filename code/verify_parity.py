# Progama que solicita uma entradas de texto e realiza a verificação de paridade.
num_error = True

while num_error:
  try:
    num = int(input("Digite o número: "))
    num_error = False
  except ValueError:
    print("\nErro: Digite apenas números inteiros\n")

if num % 2:
  parity = "ímpar"
else:
  parity = "par"

print(f"O número {num} é {parity}.")
