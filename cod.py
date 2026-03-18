from random import randint
num = randint(0, 5)
print('Bem vindo ao jogo de adivinhação!')
chance = -1
while chance!= num:
   chance = int(input('Adivinhe o número de 0 a 5 em que estou pensado:'))
   if chance == num:
         print ('Acertou! O número secreto era', num,'.')
   else:
          print ('Errado!Tente de novo.')
print('Fim do jogo. Parabéns!')