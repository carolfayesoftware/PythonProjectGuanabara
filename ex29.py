print('Será que rolou multa?\nQuanto você terá que pagar?\nChegou a hora da verdade:' )
veloc = float(input('Qual era a velocidade em que você estava dirigindo? '))
if veloc > 80:
   multa =(veloc-80)*7
   limit = veloc-80
   print('É, você vai ser multado em R${} por ter ido {}km/h acima da velocidade máxima permitida de 80km/h.'.format(multa, limit))
else:
   print('Você não foi multado.Continue dirigindo com segurança!')
