print('Então, parece que agora você quer  que eu veja o maior e menor entre três números né?\n Vou organizar e lhe dizer qual é o maior e qual é o menor!')
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número:'))
bigger =num1
small = num1
if num2 > bigger:
    bigger = num2
if num3 > bigger:
    bigger = num3
if num2 < small:
    small = num2
if num3 < small:
    small = num3
print('Entre {}, {} e {}, o maior é {} e o menor é {}.' .format(num1, num2, num3, bigger, small))