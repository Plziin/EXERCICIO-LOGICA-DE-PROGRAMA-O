num1 = int(input("digite um numero: "))
num2 = int(input("digite outro numero: "))
num3 = int(input("digite outro numero: "))
if num1 > num2:
   if num1 > num3:
      numaior = num1
      if num2 > num3:
          numeio = num2
          numenor = num3
      else:
          numeio = num3
          numenor = num2

   else:
      numaior = num3
      if num1 > num2:
          numeio = num1
          numenor = num2
      else:
          numeio = num2
          numenor = num1
else:
   if num2 > num3:
       numaior = num2
       if num1 > num3:
           numeio = num1
           numenor = num3
       else:
           numeio = num3
           numenor = num1
   else:
       numaior = num3
       if num1 > num2:
           numeio = num1
           numenor = num2
       else:
           numeio = num2
           numenor = num1


print (f"Maior numero: {numaior}")
print (f"Menor numero: {numenor}")
print (f"numero do meio: {numeio}")
