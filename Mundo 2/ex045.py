from random import randint
from time import sleep

import sys

print('''Exercício Python 045: Crie um programa que
faça o computador jogar Jokenpô com você.''')



def again():
    print(' *--* ' * 5)
    escolha = input('Quer continuar Y para sim N para não ').lower()
    if escolha == 'n':
        print("voce saiu !!")
        sys.exit(0)

while True:
    itens = ('Pedra', 'Papel', 'Tesoura')
    pc = randint(0, 2)
    print('''Suas opçoes
[0] Pedra
[1] Papel
[2] Tesoura''')
    jogador = int(input('digite sua escolha '))
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO !!!')
    sleep(1)
    print('-=' * 15)
    print('Computador Jogou {}'.format(itens[pc]))
    print('Jogador Jogou {}'.format(itens[jogador]))
    print('-=' * 15)
    if pc == 0:
        if jogador == 0:
            print('Empate')
        elif jogador == 1:
            print('Jogador Vence')
        elif jogador == 2:
            print('Computador Vence')
        else:
            print('jogada invalida')
    elif pc == 1:
        if jogador == 0:
            print('Computador Vence')
        elif jogador == 1:
            print('Empate')
        elif jogador == 2:
            print('Jogador Vence')
        else:
            print('jogada invalida')
    elif pc == 2:
        if jogador == 0:
            print('Jogador Vence')
        elif jogador == 1:
            print('Computador Vence')
        elif jogador == 2:
            print('Empate')
        else:
            print('jogada invalida')
    again()