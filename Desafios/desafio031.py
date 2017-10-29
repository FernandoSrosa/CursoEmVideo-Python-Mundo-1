print('===== DESAFIO31 =====')
'''de acordo com o trajeto da viagem calcule o valor da passagem
até 200km R$0,50 por km
acima de 200km R$0,45 por km'''

km = int(input('Qual a distancia da viagem em KM: '))
print('Valor da passagem é de:R${}'.format(km*0.50 if km<= 200 else km*0.45))