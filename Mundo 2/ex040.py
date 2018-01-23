nota1=float(input('nota 1 '))
nota2=float(input('nota 2 '))
media = (nota1+nota2)/2
if media < 5.0:
    print('sua nota {:.2f} Reprovado'.format(media))
elif media >= 5.0 and media < 7:
    print('sua nota {:.2f} Recuperaçao'.format(media))
elif media >= 7.0:
    print('sua nota {:.2f} Aprovado'.format(media))
