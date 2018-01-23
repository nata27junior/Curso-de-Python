from datetime import date
ano = date.today()
data = int(input('qual o ano de nascimento'))
idade =(ano.year)-data

#print('sua idade {}'.format(idade))
if idade <= 9:
    print('sua idade {} voce esta na categoria mirim'.format(idade))
elif idade > 9 and idade <=14:
    print('sua idade {} voce categoria infantil'.format(idade))
elif idade > 14 and idade <=19:
    print('sua idade {} voce esta na categoria junior'.format(idade))
elif idade >19 and idade <= 20:
    print('sua idades{} voce esta na catergoria senior'.format(idade))
else:
    print('sua idades{} voce esta na catergoria master'.format(idade))