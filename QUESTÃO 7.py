num = int(input("Digite um numero inteiro:"))
if num > 0:
    sinal = 'positivo'
elif num < 0:
    sinal = 'negativo'
else:
    sinal = 'nulo'
if num % 2 == 0:
    print(f"O numero {num} é par e {sinal}")
else:
    print(f"O numero {num} é impar e {sinal}")
