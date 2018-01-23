n1 = int(input('digite 1 numero '))
n2 = int(input('digite 2 numero '))
n3 = int(input('digite 3 numero '))
# verificando o menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n2 and n3 < n2:
    menor = n3
# verificando o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print(' {} é menor '.format(menor))
print(' {} é maior '.format(maior))
