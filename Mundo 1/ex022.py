nome=input('digite seu nome completo ').strip()
print('Analisando seu nome...')
print('nome maiusculo {}'.format(nome.upper()))
print('nome com todas minuscula {}'.format(nome.lower()))
print('tamanho do nome com espaços {}'.format(len(nome)))
nome2=nome.split()
print(nome2)

print('tamanho de nome sem espaços {}'.format(len(nome)-nome.count(' ')))
print('quantas letras tem primeiro nome {}'.format(len(nome2[0])))
