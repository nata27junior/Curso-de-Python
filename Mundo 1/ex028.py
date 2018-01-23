from random import randint
from time import sleep
compu = randint(0,5)
print('-=-' *20)
print('Vou pensar em um numero entre 0 e 5 . Tente adivinhar...')

print('-=-' *20)
sleep(3)
print('Pronto')
jogador = int(input('Agora digite o valor para adivinhar '))
print('PROCESSANDO....')
sleep(3)
if jogador == compu:
    print('Parabens voce adivinhou o numero era {}'.format(compu))
else:
    print('Errou o numero era {}'.format(compu))