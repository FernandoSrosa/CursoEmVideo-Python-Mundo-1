print('===== DESAFIO020 =====')
#Leia o nome de quatro alunos e gere uma ordem de apresentação aleatória

from random import shuffle

a1 = input('Nome do primeiro aluno: ')
a2 = input('Nome do segundo aluno: ')
a3 = input('Nome do terceito aluno: ')
a4 = input('Nome do quarto aluno: ')
lista = [a1, a2, a3, a4]
shuffle(lista)
print('Ordem de apredentação: {}'.format(lista))

