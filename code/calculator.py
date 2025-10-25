# Progama que solicita três entradas: Operação desejada e dois números.
op = ""

Menu = ("=== Calculadora ===\n" + "Selecione a operação:\n" + "1 - Soma\n" + "2 - Subtração\n" + "3 - Multiplicação\n" + "4 - Divisão\n" + "0 - Sair\n")
while op != 0:
  print(Menu)
  op = input("Digite a operação desejada: ")
  op_error = True

  while op_error:
    if op.isdigit():
      if int(op) >= 0 and int(op) <= 4:
        break
      else:
        print("\nERRO: Digite um número válido para a operação\n")
    else:
      print("\nERRO: A entrada precisa ser somente números\n")
    op = input("Digite a operação desejada: ")

  # 
  op = int(op)

  if op == 0:
    break

  num1_error = True
  while num1_error:
    try:
      num1 = float(input("Digite o primeiro número: "))
      num1_error = False
    except ValueError:
      print("\nErro: Digite apenas números.\n")

  num2_error = True
  while num2_error:
    try:
      num2 = float(input("Digite o segundo número: "))
      num2_error = False
    except ValueError:
      print("\nErro: Digite apenas números.\n")

  if op == 1:
    result = num1 + num2
    op_symbol = "+"
  elif op == 2:
    result = num1 - num2
    op_symbol = "-"
  elif op == 3:
    result = num1 * num2
    op_symbol = "*"
  elif op == 4:
    op_symbol = "/"
    if num2 != 0:
        result = num1 / num2
    else:
        result = "INDEFINIDO"

  print(f"Resultado: {num1} {op_symbol} {num2} = {result}\n")

