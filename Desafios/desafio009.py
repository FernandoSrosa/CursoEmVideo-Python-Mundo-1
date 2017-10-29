print('===== DESAFIO009 =====')
#Tabuada do numero digitado
n1 = int(input('Digite um numero para ver sua tabuada (do 1 ao 10): '))
n2 = n1+n1  #n2 = n1*2
n3 = n2+n1  #n3 = n1*3
n4 = n3+n1  #n4 = n1*4
n5 = n4+n1  #n5 = n1*5
n6 = n5+n1  #n6 = n1*6
n7 = n6+n1  #n7 = n1*7
n8 = n7+n1  #n8 = n1*8
n9 = n8+n1  #n9 = n1*9
n10 = n9+n1 #n10 = n1*10

print(
    '{0} x  1 = {0} \n'
    '{0} x  2 = {1} \n'
    '{0} x  3 = {2} \n'
    '{0} x  4 = {3} \n'
    '{0} X  5 = {4} \n'
    '{0} x  6 = {5} \n'
    '{0} x  7 = {6} \n'
    '{0} x  8 = {7} \n'
    '{0} x  9 = {8} \n'
    '{0} x 10 = {9}'
    .format(n1, n2, n3, n4, n5, n6, n7, n8, n9, n10)
)