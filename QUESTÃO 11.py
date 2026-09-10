lista = []
pares = []
impares = []
for _ in range (10):
    num = int(input("Digite um numero inteiro:"))
    lista.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
soma = sum(lista)
media = sum(lista) / len(lista)
maior = max(lista)
menor = min(lista)
print("\n======= RELATÓRIO ========\n")
print (f"Números informados: {lista}")
print (f"Números pares: {pares}")
print (f"Números ímpares: {impares}")
print (f"Soma dos valores: {soma}")
print (f"Média dos valores: {media:.2f}")
print (f"Maior valor: {maior}")
print (f"Menor valor: {menor}")
print ("\n===========================")
