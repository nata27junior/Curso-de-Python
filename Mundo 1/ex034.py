sal = float(input(' salario '))
if sal > 1250:
    novo= (sal*0,1)+sal
    print('novo salario R${}'.format(novo))
else:
    novo = (sal * 0,15) + sal
    print('novo salario R${:.2f}'.format(novo))