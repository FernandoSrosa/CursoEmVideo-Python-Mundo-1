print('===== DESAFIO28 =====')
'''programa gera um numero entre 0 e 5
usuario tem que adivinhar o numero'''

import random
nu = int(input('Qual numero entre 0 e 5 o computador esta pensando: '))
#num = [0,1,2,3,4,5]
#escolhido = random.choice(num)
escolhido = random.randint(0,5)
print(escolhido)
print('Acertou' if nu == escolhido else 'Errou')