from datetime import date

ano = int(input('digite um ano para analizar ou 0 para o ano atual '))
if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('\033[34m'+'O ano {} È bissexto'.format(ano))
else:
    print('\033[31m'+' O  ano {} NÃO bissexto'.format(ano))
