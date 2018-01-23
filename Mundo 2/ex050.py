from time import sleep

print('''Exercício Python 050: Desenvolva um programa que leia seis números inteiros e
mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.''')
# num = int(input("quantos numeros "))
soma = 0
cont = 0
cont2 = 0

# for c in range(0, num):
for c in range(1, 7):
    num1 = int(input("{} numeros ".format(c)))
    if num1 % 2 == 0:
        soma += num1
        cont += 1
    cont2 += 1

sleep(1)
print('voce informou {} numero e {} numeros pares e o resultado {}'.format(cont2, cont, soma))
