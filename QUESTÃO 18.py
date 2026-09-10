import random
quant = 0
for _ in range(10):
  dado1 = random.randint(1,6)
  dado2 = random.randint(1,6)
  soma = dado1 + dado2
  print(f"Valor do primeiro dado: {dado1}")
  print(f"Valor do segundo dado: {dado2}")
  print(f"Valor da soma: {soma}")
  if soma == 7:
    quant += 1

print (f"Quantidade de vezes que a som dos dados foi igual a 7: {quant}")
