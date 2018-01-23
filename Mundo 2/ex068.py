print('''Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder, 
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. ''')

from random import randint

v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Impar?[P/I] ')).strip().upper()[0]
    print(f'voce jogou {jogador} e o computador {computador}. total de {total}', end=' ')
    print('Deu par' if total % 2 == 0 else print('Deu impar'))
    if tipo == 'P':
        if total % 2 == 0:
            print('Voce Venceu')
            v += 1
        else:
            print('voce perdeu')
            break
    elif tipo == 'I':
        if total % 2 != 0:
            print('Voce venceu')
            v += 1
        else:
            print('voce perdeu')
            break
    print('Vamos jogar novamente...')
print(f'game over voce venceu {v} vezes')
