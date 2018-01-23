from math import factorial

print('''Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120''')
n = int(input('Digite um numeto para calcular fatorial: '))
f1 = factorial(n)
print('o fatorial de {} é {}'.format(n, f1))

c = n
f = 1
print('Calculando {} !'.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' X ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
