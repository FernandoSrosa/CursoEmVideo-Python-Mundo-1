import random
import emoji
from math import sqrt, floor
num = int(input("Digite um numero: "))
num = random.randint(10,20)
raiz = sqrt(num)
print('Raiz de {} quadrada é {}'.format(num, floor(raiz)))

print(emoji.emojize('Olá mundo! :earth_americas:' ,use_aliases=True))