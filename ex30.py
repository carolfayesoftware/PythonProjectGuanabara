num = float(input('Vamos descobrir se seu número é par ou ímpar!\n Digite um número: \n '))
imppar = num%2
if imppar ==1:
    print('O número {} é impar!' .format(num))
else:
    print('O número {} é par!' .format(num))
      