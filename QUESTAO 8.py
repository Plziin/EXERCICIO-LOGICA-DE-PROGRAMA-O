i = 0
soma = 0
positivos = 0
negativos = 0
pares = 0
impares = 0
while i < 10:
 num = int(input("Digite um numero inteiro"))
 i += 1
 soma += num
 if num > 0:
     positivos += 1
 else:
     negativos += 1
 if num % 2 == 0:
     pares += 1
 else:
     impares += 1
media = soma / 10
print (f"A soma total: {soma}")
print (f"A quantidade de positivos: {positivos}")
print (f"A quantidade de negativos: {negativos}")
print (f"A quantidade de números pares: {pares}")
print (f"A quantidade de números impares: {impares}")
print (f" Média = {media}")
