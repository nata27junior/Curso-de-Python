#manipulando string
#fatiamento
frase = 'curso EM video python'
print(frase[9])
print(frase[9:14])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])
#analise
print('len de frase :{}'.format(len(frase)))
print('contando "o" {}'.format(frase.count('o')))
print('contando "o" com fatiamento {}'.format(frase.count('o',0,14)))
print('quantas vezes encontra deo {}'.format(frase.find('deo')))
print('nao encontra android {}'.format(frase.find('android')))
print('tem curso em frase {}'.format('curso' in frase))
print('substituindo pytoh por {}'.format(frase.replace('python','androi')))
print('transformando tudo em maiusculo {}'.format(frase.upper()))
print('tranformando tudo em minusculo {}'.format(frase.lower()))
print('primeira letra em maiusculo {}'.format(frase.capitalize()))
print('primeiras letras maiusculo {}'.format(frase.title()))

frase2 ='    aprenda python   '
print('removendo espaço exedente {}'.format(frase2.strip()))
print('removendo espaço exedente no final {}'.format(frase2.rstrip()))
print('removendo espaço exedente no inicio {}'.format(frase2.lstrip()))

print('retirando espaço {}'.format(frase.split()))
print ('juntando com - {} '.format('-'.join(frase)))



