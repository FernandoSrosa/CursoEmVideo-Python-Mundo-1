print('===== DESAFIO33 =====')
#leia tres numeros e mostre o maior e o menor deles

n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
n3 = int(input('Terceiro numero: '))

''' METODO 1
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
'''

'''Metodo 2 '''
if n1 > n2:
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1
if n3 > maior:
    maior = n3
if n3 < menor:
    menor = n3
print('\nMaior {} \nMenor {}'.format(maior, menor))