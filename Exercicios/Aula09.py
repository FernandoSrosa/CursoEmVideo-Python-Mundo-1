frase = 'Curso em Video Python'

#printa a casa 9 da string
print(frase[9])

#ptinra o intervalo do primeiro argumento declarado até o anterior ao ultimo declarado
print(frase[9:14])

#printa o intervalo do primeiro argumento declarado até o anterior ao ultimo declarado
#pulando o intervalo informado no terceiro argumento
print(frase[9:14:2])

#printa os caracteres até o argumento informado
print(frase[:5])

#printa os caracteres do argumento até o final
print(frase[:15])

###########transformação

print(len(frase))
'''mostra a quatidade de caracteres'''
print(frase.count('o'))
'''conta a quantidade de ocorrencias da variavel informada'''
print(frase.count('o',0,13))
'''conta a quantidade de ocorrencias da variavel dentro do intervalo'''
print(frase.find('deo'))
'''mostra em qual caractere começa a cadeia informada
caso nao exista corespodencia, retorna -1'''
print('Curso' in frase)
'''retorna true ou false se a cadeia informada existir na cadeia'''
frase.replace('Phyton','Android')
'''troca o primeiro argumento pelo segundo dentro da cadeia'''
frase.upper()
'''muda os caracteres para maisculas'''
frase.lower()
'''muda os caraceres para minusculas'''
frase.capitalize()
'''muda os caracteres para minusculas e o primeiro caracter da frase para maiusla'''
frase.title()
'''muda os caracteres para minusculas e o primeiro caracter de cada palavra pra maiuscula'''
frase.strip()
'''remove espaços no começo e no final da cadeia (desnecessarios
variação de: rstrip(right) lstrip(left) apagando os espaços de apenas uma estremidade'''


################divisão
frase.split()
#divide a cadeia seguindo os espaços como ponto de divisao gerando novas listas
'-'.join(frase)
#gera uma string juntando as separadas usando o caracter definido como marcaçao das separações
