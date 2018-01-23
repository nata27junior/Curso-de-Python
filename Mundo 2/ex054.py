from datetime import date

print('''Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e 
quantas já são maiores.''')
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('Ano da pessoa {}° nasceu '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo timemos {} pessoas maiores de idade'.format(totmaior))
print('Ao todo timemos {} pessoas menore de idade'.format(totmenor))
