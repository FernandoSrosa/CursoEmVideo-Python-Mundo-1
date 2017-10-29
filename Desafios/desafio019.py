print('===== DESAFIO019 =====')
#sorteie um dos 4 alunos para apagar o quadro

import random

a1 = input('Nome do primeiro aluno: ')
a2 = input('Nome do segundo aluno: ')
a3 = input('Nome do terceito aluno: ')
a4 = input('Nome do quarto aluno: ')
lista = [a1, a2, a3, a4]
sort = random.choice(lista)
print('Aluno escolhido: {}'.format(sort))