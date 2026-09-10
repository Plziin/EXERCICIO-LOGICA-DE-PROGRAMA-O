import math
num = float(input("Digite um número real: "))
raiz = math.sqrt(num)
absolute = abs(num)
up = math.ceil(num)
under = math.floor(num)
print(f"Raiz quadrada: {raiz}")
print(f"Valor absoluto: {absolute}")
print(f"Arredondamento para cima: {up}")
print(f"Arredondamento para baixo: {under}")
if num.is_integer() and num >= 0:
 fatorial = math.factorial(int(num))
 print(f"Fatorial: {fatorial}")
else:
     print("Não é possivel calcular o fatorial desse numero: ")
