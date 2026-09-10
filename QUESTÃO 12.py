lista = []
for _ in range (5):
    prod = str(input('Digite um produto: '))
    preco = float(input('Digite um valor: '))
    quant = int(input('Digite a quantidade de produtos: '))
    produtos = {
        "Nome": prod,
        "Preco":preco,
        "Quantidade":quant
    }
    lista.append(produtos)
    maior = max(lista,key=lambda p: p["Preco"])
    total = 0
    for produtos in lista:
        total += produtos["Preco"] * produtos["Quantidade"]
print("=============== RELATÓRIO ===================")
print (f"Produtos Cadastrados:")
for produtos in lista:
    print(f"- {produtos['Nome']}")
print (f"Valor do estoque: {total:.2f}")
print (f"Maior preço unitário: {maior['Nome']} (R$ {maior['Preco']})")
