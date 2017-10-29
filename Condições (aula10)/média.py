n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('Sua média foi {:.1f}'.format(m))
print('Parabens!' if m>=6 else 'Precisa estudar mais!')