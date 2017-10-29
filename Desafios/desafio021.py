print('===== DESAFIO021 =====')
#Faça um programa que reproduza um audio .mp3 dentro do programa


from pygame import mixer
mixer.init()
mixer.music.load('teste.mp3')
mixer.music.play()
input('Agora você escuta?')

