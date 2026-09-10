lista = []
for temp in range (1, 8):
    temp += 1
    temp = float(input("Digite um numero de temperatura: :"))
    lista.append(temp)
maior = max(lista)
menor = min(lista)
media = sum(lista) / len(lista)
diacima = 0
for temp in lista:
    if temp > media:
        diacima += 1
print (f"Maior temperatura: {maior}C")
print (f"Menor temperatura: {menor}C")
print (f"Media da temperatura: {media:.2f}C")
print (f"Dias acima da média: {diacima}")
