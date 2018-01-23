from random import randint
from time import sleep
print('\033[1;34m-=\033[m'*20)
print('\033[1;36m VOU PENSAR EM UM NÚMERO DE 0 A 10 \033[m')
print('\033[1;34m-=\033[m'*20)
ns = randint(0, 10)
resp = int(input('\033[1;35m Tente Adivinhar: '))
cont = 1
while(resp!=ns):
    resp = int(input('Tente novamente: '))

    if resp < ns:
        print('\033[1;31m Maior... \033[m')
    elif resp > ns:
        print('\033[1;34m Menor... \033[m')
    cont = cont + 1
print('\033[1;35mPROCESSANDO...\033[m')
sleep(2)
print('\033[1;34m O número era {}, e você o acertou com {} tentativas\033[m'.format(ns, cont))