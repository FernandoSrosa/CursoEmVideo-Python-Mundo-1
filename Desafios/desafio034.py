print('===== DESAFIO34 =====')
''''calcule o aumento de acordo com o salario
maior que 1250 reais = 10% de aumento
menor = 15%'''

sal = float(input('Qual é o salario R$: '))
if sal > 1250.00:
    nsal = sal * 1.1
else:
    nsal = sal * 1.15
print('Novo salario: R${:.2f}'.format(nsal))
