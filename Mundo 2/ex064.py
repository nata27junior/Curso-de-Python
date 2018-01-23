print('''Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles 
(desconsiderando o flag).''')
n1 = numero = cont = soma = 0
numero = int(input('Digite um numero[999 para parar]: '))
#n1= int(input('Primeiro valor'))
while numero != 999:
    soma += numero
    #soma += n1
    cont += 1
    #n1 = int(input('Primeiro valor'))
    numero = int(input('Digite um numero[999 para parar]: '))
print('Acabou voce digitou {} numero e a soma foi {}'.format(cont,soma))
#print('O maior {} e o menor {}'.format(cont, soma))
