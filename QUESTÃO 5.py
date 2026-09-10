while True:
    try:
        idade = int(input("digite sua idade: "))
        if idade >= 0:
           break
        else:
           print ("ERRO, TENTE NOVAMENTE: ")
    except ValueError:
      print("DIGITE O VALOR INTEIRO POISTIVO:")
if idade <= 12:
      situacao = 'criança'
elif idade <= 17:
      situacao = 'adolescente'
elif idade <= 59:
      situacao = 'adulto'
else:
      situacao = 'idoso'

print (f"idade = {idade} ")
print (f"Situação = {situacao}")
