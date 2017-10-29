n1 = int(input('Numero 1 '))
n2 = int(input('Numero 2 '))

print ('Soma {}'.format(n1+n2), end=' ')
print ('Subtração {}'.format(n1-n2), end=' ')
print ('Multiplicação {}'.format(n1*n2), end=(' '))
print ('Divisão {}'.format(n1/n2), end=(' '))
print ('Potencia {}'.format(n1**n2), end=(' '))
print ('Divisão inteira {}'.format(n1//n2), end=(' '))
print ('Esponencial {}'.format(n1%n2), end=(' '))

# Prdem de precedencia
# 1 ()
# 2 **
# 3 * / // %
# 4 + -