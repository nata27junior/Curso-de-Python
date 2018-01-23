num1=int(input('digite um numero'))
num2=int(input('digite outro um numero'))
if num1 > num2:
    print("primeiro numero é mairo")
    print('numero {} maior que {}'.format(num1,num2))
elif num2 > num1:
    print("segundo numero é mairo")
    print('numero {} maior que {}'.format(num2,num1))
elif num1 == num2:
    print('nao existe valor maior numero {} é igual {}'.format(num1,num2))
