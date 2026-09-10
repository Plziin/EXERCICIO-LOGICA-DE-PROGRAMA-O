lista = []
while True:
  print("===================================")
  print("  GERENCIAMENTO DE NÚMEROS  ")
  print("===================================")
  print("1 - Cadastrar número")
  print("2 - Listar numeros")
  print("3 - Exibir maior numero")
  print("4 - Exibir menor numero")
  print("5 - Calcular média")
  print("0 - sair")
  opcao = int(input("Digite a opcao desejada:"))
  if opcao == 1:
    num = float(input("Informe um numero: "))
    lista.append(num)
    print("Número cadastrado com sucesso")
  elif opcao == 2:
    if len(lista) == 0:
        print("Nenhum número cadastrado")
    else:
        print(f"Números cadastrado: {lista}")

  elif opcao == 3:
    if len(lista) == 0:
        print("Nenhum número cadastrado")
    else:
        print("Maior número:", max(lista))

  elif opcao == 4:
    if len(lista) == 0:
        print("Nenhum número cadastrado")
    else:
        print("Menor número:", min(lista))

  elif opcao == 5:
    if len(lista) == 0:
        print("Nenhum número cadastrado")
    else:
        media = sum(lista) / len(lista)
        print(f"Média: {media}")
  elif opcao == 0:
    print("Programa finalizado com sucesso")
    break
  else:
    print("Opção invalida, Tente novamente: ")
