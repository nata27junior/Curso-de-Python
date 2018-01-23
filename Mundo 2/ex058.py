from random import randint

print('''Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
 Só que agora o jogador vai tentar adivinhar até acertar, 
 mostrando no final quantos palpites foram necessários para vencer.''')
computador = randint(0, 10)
print('sou seu computador... acabei de pensat em um numero entre 0 e 10')
print('sera que voce adivinha qual foi')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('qual seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais .. tente mais uma vez')
        elif jogador > computador:
            print('Menos... tente mais uma vez')

print('acertou com {} tentativas . parabens'.format(palpites))
