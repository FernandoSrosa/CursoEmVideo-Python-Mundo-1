print('===== DESAFIO036 =====')
#leia o cumplimento de 3 retas e verifique se ela pode formar um triangulo

r1 = float(input('Cumprimento da primeira reta: '))
r2 = float(input('Cumprimento da segunda reta: '))
r3 = float(input('Cumprimento da terceira reta: '))

'''if r1 > r2:
    maior = r1
else:
    maior = r2
if r3 > maior:
    maior = r3

if (r1 + r2 + r3 - maior) > maior:
    print('Forma um tringulo')
else:
    print('Não forma um triangulo')'''

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('Formam um triangulo')
else:
    print('As retas não formam um triangulo')
