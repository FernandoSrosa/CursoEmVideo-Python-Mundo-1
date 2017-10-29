print ('===== DESAFIO007 =====')
#Leia um numero e mostre o seu sobro, seu triplo e sua raiz quadrada

from math import sqrt

n1 = int(input('Digite um numero: '))
print('Sobre {}: \nSeu dobro é {} \nSeu triplo é {} \nSua raiz quadrada é {:.3f}'
       .format(n1, n1*2, n1*3, sqrt(n1)))