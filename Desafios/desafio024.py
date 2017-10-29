print('===== DESAFIO24 =====')
#mostre se o nome da cidade começa com 'Santo'
cid = str(input('Digite o nome da sua cidade: ')).strip().title()
c = cid.split()
print('Nome da cidade começa com "Santo"? {}'.format('Santo' in c[0]))