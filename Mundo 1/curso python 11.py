print('\033[0;33;44mOlá Mundo\033[m')  # sem estilo
print('\033[1;33;44mOlá Mundo\033[m')  # em negrito
print('\033[4;33;44mOlá Mundo\033[m')  # sublinhado
print('\033[7;33;44mOlá Mundo\033[m')  # negative inverte
# text 30-37 # back 40-47
print('\033[0;30;41mOlá Mundo\033[m')
print('\033[4;33;44mOlá Mundo\033[m')
print('\033[1;35;43mOlá Mundo\033[m')
print('\033[30;42mOlá Mundo\033[m')
print('\033[mOlá Mundo\033[m')
print('\033[7;30mOlá Mundo\033[m')
print('\033[7;30mOlá Mundo\033[m\033[30;42mOlá Mundo\033[m')
print('\033[0;30;41mOlá Mundo\033[m\033[30;42mOlá Mundo\033[m')
m = 'aprendi a colocar cores'
s = 'sera mesmo'
cores = {'limpa':'\033[m','azul': '\033[34m','amarelo':'\033[33m','pb':'\033[7;30m'}
print('AQUI {} {} {} {} {}'.format('\033[0;34m', m, '\033[1;30;41m', s, '\033[m'))
print('AQUI {} {} {} {} {}'.format(cores['amarelo'],m,cores['pb'],s,cores['limpa']))
