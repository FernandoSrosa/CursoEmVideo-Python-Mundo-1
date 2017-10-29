print('===== DESAFIO008 =====')
#Leia um valor em metros e o exiba convertido para centimetros e milímetros
n1 = int(input('Digite um valor em metros: '))

km = n1/1000
hm = n1/100
dam = n1/10
m = n1
dc = n1*10
cm = n1*100
mm = cm*1000
print('{} metros equivalem a: \n{}km \n{}hm \n{}dam \n{}m \n{}dc \n{}cm \n{}mm'.format(n1, km, hm, dam, m,dc, cm, mm))