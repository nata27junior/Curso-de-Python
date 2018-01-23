numero = int(input('digita um numero'))
escolha= int(input("para conversao em:\nbinario digite 1\npara octal 2\npara hexadecimal 3"))
if escolha ==1:
    binario = bin(numero)
    print ('seu numero {}, em binario {}'.format(numero,binario[2:]))
elif escolha ==2:
    octal = oct(numero)
    print('seu numero {}, em octal {}'.format(numero, octal[2:]))
elif escolha == 3:
    hexa = hex(numero)

    print ('seu numero {}, em hexadecimal {}'.format(numero,hexa[2:]))

else:
    print ('opçao invalida')
