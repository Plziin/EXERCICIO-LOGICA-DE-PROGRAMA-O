lista = []
for _ in range (5):
    nome = str(input("Digite o nome: "))
    estado = str(input("Digite o estado em sigla: "))
    while True:
        populacao = int(input("Digite o numero da população estimada: "))
        if populacao >= 0:
             break
        else:
            print ("Número invalido,Digite novamente: ")

    info = {
        "Nome": nome,
        "Estado": estado,
        "Populacao": populacao
    }
    lista.append(info)
maior = max(lista, key=lambda x: x["Populacao"])
menor = min(lista, key=lambda x: x["Populacao"])
total = sum(cidade["Populacao"] for cidade in lista)
media = total / len(lista)
print(f"Cidade com maior populacao: {maior['Nome']}")
print(f"Cidade com menor populacao: {menor['Nome']}")
print(f"População total das cidades: {total} pessoas")
print(f"Média populacional: {media:.2f} de pessoas")
for cidade in lista:
 print(f"Dados completos: {cidade['Nome']} || {cidade['Estado']} || {cidade['Populacao']}")
