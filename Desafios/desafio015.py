print('===== DESAFIO015 =====')
#Calcule o preço do aluguem do carra sabendo que:
#cada dia custa 60 reais
#e cada km rodado custa 15 centravos
from math import ceil
d = float(input('Quantos dias o carro foi alugado: '))
km = float(input('Quatos quilometros foram rodados: '))
p = (d * 60) + (km * 0.15)
print('O valor a pagar pelo aluguel é de R${:.2f}'.format(p + 0.00499))
print('O valor a pagar pelo aluguel é de R${}'.format(p))