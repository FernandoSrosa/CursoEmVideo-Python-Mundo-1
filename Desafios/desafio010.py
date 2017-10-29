print('===== DESAFIO010 =====')
#Leia valor em real e converta apra dolar
print('Separar os centavos com (.)')
din = float(input('Quantos reais o sr(a) possue? '))
dol = float(input(('Qual a tava de conversão do Dolar? ')))
#consere tava de conversão de 3.27
print('{:.2f} reais equivalem a {:.2f} dolares.'.format(din, din/dol))