i = 1
notas = []
while i <= 3:
     nota = float(input(f"Digite a {i} nota (0 a 10) :"))
     if nota >= 0 and nota <= 10:
        notas.append(nota)
        i += 1
     else:
        print ('ERRO, VALOR INVÁLIDO, TENTE NOVAMENTE')
media = (notas[0] + notas[1] + notas[2]) / 3
if media >= 7:
  situacao = 'APROVADO'
elif media >= 5:
    situacao = 'RECUPERAÇÃO'
else:
    situacao = 'REPROVADO'
print ("\n=======RESULTADOS========")
print(f"primeira nota = {notas[0]}")
print(f"segunda nota = {notas[1]}")
print(f"terceira nota = {notas[2]}")
print(f"media = {media}")
print (f"situação: {situacao} ")
