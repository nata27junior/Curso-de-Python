from datetime import date

atual = date.today().year
nasc = int(input('qual o ano de nascimento'))
sexo = input('qual o seu sexo M masculino F feminino').lower()

idade = atual - nasc
if sexo =="m":
    print('quem nasceu em  {} tem {} anos em {}'.format(nasc, idade, atual))
    if idade < 18:
        saldo = 18 - idade
        print('ainda falta {} anos para alistamento'.format(saldo))
        ano = atual + saldo
        print('sua idade {} voce ainda vai se alistar em {}'.format(idade, ano))
    elif idade == 18:
        print('voce tem que se alistar imediatamente')
        print('sua idade {} voce esta na hora  de se alistar'.format(idade))
    else:
        saldo = idade - 18
        print('voce ja deveria ter se alistado ha {} anos'.format(saldo))
        ano = atual - saldo
        print('sua idade {} voce passou da idade para se alistar em {}'.format(idade, ano))
else:
    print('Voce é do sexo Feminino nao se alista')
    print('quem nasceu em  {} tem {} anos em {}'.format(nasc, idade, atual))

