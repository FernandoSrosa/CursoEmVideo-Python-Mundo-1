print('===== DESAFIO22 =====')
''''Leia o nome completo da pessoa e msotre
com todas as letras maiusculas
com todas as letras minusculas
quantas letras tem (sem espaço)
quantas letras tem o primeiro nome'''

nome = str(input('Digite seu nome completo: ')).strip()
div = nome.split()
print(nome.upper())
print(nome.lower())
print(len(nome.replace(' ', '')))
print(div[0].capitalize(), 'tem:',len(div[0]),'letras.')