print('===== DESAFIO032 =====')
#leia um ano e verifique se ele é bissexto
# multiplo de 4 é bisexto
# menos se for multiplo de 100
# se for multiplo de 100 e de 400 é bissexto

from datetime import date
ano = int(input('Digite o ano(0 para ano atual): '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0.000 or ano % 400 == 0.000:
    print('Ano bissexto')
else:
    print('Não é bissexto')