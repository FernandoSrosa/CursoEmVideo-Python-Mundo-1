nome = str(input('Qual é o seu nome? '))
print('Olá {:>20}!'.format(nome))
print('Olá {:<20}!'.format(nome))
print('Olá {:^20}!'.format(nome))
print('Olá {:=^20}!'.format(nome))
print('Olá {:-^20}!'.format(nome))
print('Olá {:*^20}!'.format(nome))
print('Olá {:|^20}!'.format(nome))

n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
so = n1 + n2
su = n1 - n2
d = n1 / n2
m = n1 * n2
di = n1 // n2
e = n1 ** n2
print('Soma {}, Subtração {}, Divisão {:.3f}, Multiplicação {} Divisão Inteira {}, Esponencial {}'
      .format(so, su, d, m, di, e))
