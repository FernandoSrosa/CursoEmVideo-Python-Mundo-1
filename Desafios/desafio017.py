print('===== DESAFIO017 =====')
#Leia o comprimenteo dos catetos e calcule a hipotenusa
from math import sqrt,hypot
ca = float(input('Qual o comprimento do cateto adjacente: '))
co = float(input('Qual o comprimento do cateto oposto: '))
# h = sqrt((ca**2) + (co**2))
h = hypot(ca, co)
print ('A hipotenusa desse triangulo mede {}'.format(h))
