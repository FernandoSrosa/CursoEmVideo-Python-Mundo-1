print('===== DESAFIO26 =====')
'''mostre quantas letras "A" possue na frase
e qual a possição da ultima ocorrencia'''

f = str(input('Digite uma frase: ')).strip()
f1 = f.upper()
print('A frase possue {} letras "A"'.format(f1.count('A')))
print('Sua primeira ocorrencia é na {} letra'.format(1+(f1.find('A'))))
print('Sua ultima ocorencia é na {} letra'.format(1+f1.rfind(('A'))))