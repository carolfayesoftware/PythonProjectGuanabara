from random import randint
num = randint(0, 5)
print('Bem vindo ao jogo de adivinhação do mago supremo!')
chance = -1
while chance!= num:
   chance = int(input('Adivinhe o número de 0 a 5 em que estou pensado:'))
   if chance == num:
         print ('Acertou! O número secreto era', num,'.')
   elif chance >=6 :
        print('Você colocou um número que não está na lista de opções! Toma um doce e tenta mais uma vez. ')     
   else:
          print ('Errado!Tente de novo.')
print('Fim do jogo. Parabéns!')