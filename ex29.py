print('Será que rolou multa?\nQuanto você terá que pagar?\nChegou a hora da verdade:' )
veloc = float(input('Qual era a velocidade em que você estava dirigindo? '))
if veloc > 80:
   multa =(veloc-80)*7
   limit = veloc-80
   print('É, você vai ser multado em R${} por ter ido {}km/h acima da velocidade máxima permitida.'.format(multa, limit))
else:
   print('Parabéns, você não foi multado.')