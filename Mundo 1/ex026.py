fr= str(input('digite a frase ').lower().strip())#converte em minusculo e corta os espaços
n=str(input('digite a letra '))
print('A letra {} aparece {} vezes  na frase'.format(n,fr.count(n)))
print(' A primeira letra {} apareceu na posiçao {}'.format(n,fr.find(n)+1))
print(' A ultima letra {} apareceu na posiçao {}'.format(n,fr.rfind(n)+1))
