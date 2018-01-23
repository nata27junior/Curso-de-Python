from random import choice,randint
from datetime import date
ano = date.today().year
print(ano)
num = '7'
res = int(num) / 2
print(type(res))
valor = '153'
parte = "5"
valor += parte
print(valor.isnumeric())
n = [2, 5, 9, 1, 4]
res = choice(n) % n[0]
print(res)
num = randint(1, 6)
res = num // 2
print('esse')
print(res)
frase = 'Curso em Video de Python'
separado = frase.split()
palavra = separado[2]
letra = palavra[3]
print(letra.upper())

preço = int(input('preço'))
novo = preço + 50 if preço < 1000 else preço - 35
print(novo)
novo = +50 if preço < 1000 else +35
print(novo)