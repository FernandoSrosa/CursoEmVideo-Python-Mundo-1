print('===== DESAFIO011 =====')
#Leia a largura e a altura de uma parede, calcule a sua area
# e a quantidade de tinta necessaria para pinta-la
# sabendo que cada litro de tinta pinta 2m²

h = float(input('Altura da parede: '))
l = float(input('Largura da parede: '))
a = float(h * l)
tin = a / 2
print('Essa parede tem {:.2f}m²'.format(a))
print('Seram necessarios {:.2f} litros de tinta'.format(tin))