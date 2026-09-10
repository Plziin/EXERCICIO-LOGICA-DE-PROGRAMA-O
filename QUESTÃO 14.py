lista = []
for _ in range(5):
    nome = str(input("Digite o nome do aluno: "))
    while True:
        nota = float(input("Digite sua nota do aluno: "))
        if 0 <= nota <= 10:
             break
        else:
            print("Nota do aluno invalida, Digite uma nota entre 0 e 10")
    while True:
        nota2 = float(input("Digite sua nota do aluno: "))
        if 0 <= nota2 <= 10:
             break
        else:
            print ("Nota inválida, Digite uma nota entre 0 e 10")
    while True:
        nota3 = float(input("Digite sua nota do aluno: "))
        if 0 <= nota3 <= 10:
            break
        else:
            print("Nota inválida, Digite uma nota entre 0 e 10")
    media = (nota + nota2 + nota3) / 3

    atributos ={
        "Nome": nome,
        "Nota1": nota,
        "Nota2": nota2,
        "Nota3": nota3,
        "media": media
        }
    lista.append(atributos)
maior = max(lista, key=lambda x: x["media"])
menor = min(lista, key=lambda x: x["media"])
aprovados = 0
recuperacao = 0
reprovados = 0
for aluno in lista:
    if aluno["media"] >= 7:
        aprovados += 1
    elif aluno["media"] >= 5:
        recuperacao += 1
    else:
        reprovados += 1
    print(f"Nome: {aluno['Nome']} || Média: {aluno['media']} ")
print(f"Estudante com maior média: {maior['Nome']}")
print(f"Estudante com menor média: {menor['Nome']}")
print(f"Quantidade de aprovados: {aprovados}")
print(f"Quantidade de recuperacao: {recuperacao}")
print(f"Quantidade de reprovados: {reprovados}")
