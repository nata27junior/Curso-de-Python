print('''Exercício Python 053: Crie um programa que leia uma frase qualquer 
e diga se ela é um palíndromo, desconsiderando os espaços.
Exemplos de palíndromos:
APOS A SOPA, 
A SACADA DA CASA, 
A TORRE DA DERROTA, 
O LOBO AMA O BOLO,
ANOTARAM A DATA DA MARATONA.
''')
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
inverso2 = junto[::-1]
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('temos um palindromo')
else:
    print(' nao é palindromo')
if inverso2 == junto:
    print('temos um palindromo')
else:
    print(' nao é palindromo')