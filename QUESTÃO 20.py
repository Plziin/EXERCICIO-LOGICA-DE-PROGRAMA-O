lista = []
while True:

 print("======================================== ")
 print("   SISTEMA ACADÊMICO   ")
 print("======================================== ")
 print("1 - Cadastrar Estudante ")
 print("2 - Listar Estudantes ")
 print("3 - Consultar Estudante ")
 print("4 - Alterar Dados ")
 print("5 - Remover Estudante ")
 print("6 - Gerar Relatório da Turma ")
 print("0 - Sair do Programa ")

 opcao = int(input("Digite a opção Desejada: "))
 if opcao == 1:
    notas = []
    nome = str(input("Digite o nome do estudante: "))
    idade = int(input("Digite a idade: "))
    curso = str(input("Digite o nome do curso: "))
    for _ in range(3):
        nota = float(input("Digite sua nota: "))
        notas.append(nota)
    media = sum(notas) / len(notas)
    if media >= 7:
        situacao = "aprovado"
    elif media >= 5:
        situacao = "recuperacao"
    else:
        situacao = "reprovado"
    aluno = {
        "nome": nome,
        "idade": idade,
        "curso": curso,
        "notas": notas,
        "media": media,
        "situacao": situacao
    }
    lista.append(aluno)
    print("Aluno Cadastrado com Sucesso! ")
 elif opcao == 2:
   if len(lista) == 0:
       print("Nenhum Aluno Cadastrado ")
   else:
       for aluno in lista:
        print("\n=== LISTA DE ESTUDANTES ===")
        print(f"Aluno: {aluno['nome']}")
        print(f"Idade: {aluno['idade']}")
        print(f"Curso: {aluno['curso']}")
        print(f"Notas: {aluno['notas']}")
        print(f"media: {aluno['media']:.2f}")
        print(f"situacao: {aluno['situacao']}")
 elif opcao == 3:
    estudante = str(input("Digite o nome do estudante: "))
    encotrado = False
    for aluno in lista:
       if aluno['nome'] == estudante:
           print(f"Nome: {aluno['nome']}")
           print(f"Idade: {aluno['idade']}")
           print(f"Curso: {aluno['curso']}")
           print(f"Notas: {aluno['notas']}")
           print(f"media: {aluno['media']:.2f}")
           print(f"situacao: {aluno['situacao']}")
           encotrado = True
           break
    if not encotrado:
      print("Aluno não encontrado")
 elif opcao == 4:
    busca = str(input("Digite o nome do estudante para alterar os dados: "))
    encotrado4 = False

    for aluno in lista:
        if aluno['nome'] == busca:
            print(f"Nome: {aluno['nome']}")
            print(f"Idade: {aluno['idade']}")
            print(f"Curso: {aluno['curso']}")
            print(f"Notas: {aluno['notas']}")
            print(f"Média: {aluno['media']:.2f}")
            print(f"Situação: {aluno['situacao']}")

            novonome = input("Digite o novo nome (ou Enter para manter): ")
            if novonome != "":
                aluno['nome'] = novonome

            novaidade = input("Digite a nova idade (ou Enter para manter): ")
            if novaidade != "":
                aluno['idade'] = int(novaidade)

            novocurso = input("Digite o novo curso (ou Enter para manter): ")
            if novocurso != "":
                aluno['curso'] = novocurso

            novanota = input("Deseja alterar as notas do estudante? (s/n): ")
            if novanota.lower() == "s":
                notas = []
                for _ in range(3):
                    nota = float(input("Digite a nova nota: "))
                    notas.append(nota)
                aluno['notas'] = notas
                aluno['media'] = sum(notas) / len(notas)
                if aluno['media'] >= 7:
                    aluno['situacao'] = "Aprovado"
                elif aluno['media'] >= 5:
                    aluno['situacao'] = "Recuperação"
                else:
                    aluno['situacao'] = "Reprovado"

            print("Dados alterados com sucesso!")
            encontrado4 = True
            break

    if not encontrado4:
            print("Estudante não encontrado")

 elif opcao == 5:
       encontrado5 = False
       removido = input("Digite o nome do estudante que desejs remover: ")
       for aluno in lista:
        if aluno['nome'] == removido:
          lista.remove(aluno)
          print(f"Aluno removido! ")
          encontrado5 = True
          break
        if not encontrado5:
           print ("Aluno não encontrado")
 elif opcao == 6:
     if len(lista) == 0:
      print("Aluno Inexistente! ")

     else:
         aprovados = 0
         recuperacao = 0
         reprovados = 0

         for aluno in lista:
             if aluno['situacao'] == 'aprovado':
                 aprovados += 1
             elif aluno['situacao'] == 'recuperacao':
                 recuperacao += 1
             else:
                 reprovados += 1

         maior = max(lista, key=lambda x: x['media'])
         menor = min(lista, key=lambda x: x['media'])
         mediageral = sum([aluno['media'] for aluno in lista]) / len(lista)

         print(f"Totoal de alunos cadastrados:{len(lista)}")
         print(f"Aprovados: {aprovados}")
         print(f"Recuperacao: {recuperacao}")
         print(f"Reprovados: {reprovados}")
         print(f"Maior média: {maior['media']:.2f} (Aluno: {maior['nome']})")
         print(f"Menor media: {menor['media']:.2f} (Aluno: {menor['nome']})")
         print(f"Média Geral: {mediageral:.2f}")
