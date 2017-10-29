print('===== DESAFIO029 =====')
'''se a velocidade do carro ultrapassar 80km\h ele sera multado
o valor da multa sera de 7reais por km acima do limite'''

km = int(input('Qual a velocidade do carro: '))
if km>80:
    print('MULTADO')
    multa = float((km-80)*7)
    print('Valor da multa R${:.2f}'.format(multa))
print('Tenha um bom dia, dirija com segurança!')
