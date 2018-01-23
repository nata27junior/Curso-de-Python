print('''Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida''')
peso= float(input('digite seu peso '))
altura= float(input('digite sua altura em metros '))
imc = peso /(altura ** 2)
if imc <= 18.5:
    print('o seu imc é {:.2f} abaixo do peso'.format(imc))
    #print("o seu imc é " + str(imc))
    #print('Abaixo do peso')

elif imc > 18.5 and imc <= 25:#18.5<imc<=25
    print('o seu imc é {:.2f} Peso ideal'.format(imc))
elif imc > 25 and imc <= 30:
    print('o seu imc é {:.2f} Sobrepeso'.format(imc))
elif imc > 30 and imc <= 40:
    print('o seu imc é {:.2f} obesidade'.format(imc))
else:
    print('o seu imc é {:.2f} obesidade morbida'.format(imc))