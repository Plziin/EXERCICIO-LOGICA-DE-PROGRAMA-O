nome = str(input ('Qual o seu nome?'))
while True:
    try:
        idade = int(input ('Qual a sua idade?'))
        if idade < 0:
            print (" A idade não pode ser negativa:")
        else:
            break
    except ValueError:
        print("Digite um valor inteiro para a idade:")
while True:
    try:
        altura = float(input ('Qual a sua altura?'))
        break
    except ValueError:
        print("Digite um numero decimal para a altura para a altura:")
local = str(input ('Qual a sua cidade?'))
print("====== CARTÂO DE IDENTIFICAÇÃO ======")
print (f"Nome: {nome}")
print (f"idade: {idade}")
print (f"altura: {altura}")
print (f"cidade: {local}")

