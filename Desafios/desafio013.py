print('===== DESAFIO013 =====')
#aplique 15% de aumento no salario do funcionário
old = float(input('Informe seu salário atual: R$'))
new = float(old + (old/100) * 15)
print('Seu salario foi acrescido em 15%, seu novo salário sera: R${:.2f}'.format(new))