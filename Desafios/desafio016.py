print('===== DESAFIO016 =====')
#Leia um numero real e mostre sua porção inteira

import math

n1 = float(input('Digite um numero real: '))
print ('A parte inteira desse numero é {}'.format(int(n1)))
print ('A parte inteira desse numero é {}'.format(math.trunc(n1)))
print ('A parte inteira desse numero é {:.0f}'.format(n1))