lista = []
for _ in range(5):
    nome = str(input("Digite o nome do produto: "))
    telefone = int(input("Digite o telefone: "))
    email = str(input("Digite o email: "))
    agenda = {
        "Nome": nome,
        "Telefone": telefone,
        "Email": email,
    }
    lista.append(agenda)
consulta = str(input("Digite o nome para consulta: "))
for contato in lista:
    if contato["Nome"].lower() == consulta.lower():
        print(f"Nome:{contato['Nome']}")
        print(f"Telefone: {contato['Telefone']}")
        print(f"Email: {contato['Email']}")
else:
    print ("Contato não encontrado")
