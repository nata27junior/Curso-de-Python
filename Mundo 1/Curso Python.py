
import emoji
print(emoji.emojize("Olá, mundo :earth_americas:" , use_aliases=True))
print('================Desafio 01===================')
nome=input('Qual é seu nome?')
print("Olá {}! Prazer em te conhecer!".format(nome))




print('====== DESAFIO 02 ======')
dia=input('Dia =')
mes=input('Mês =')
ano=input('Ano')
print('Vocês nasceu no dia {} de {} de {}. Correto?'.format(dia,mes,ano))



print('===== Desafio 3 =====')
print('Escreva os números para soma')
n1=input('Primeiro número >')
n2=input('Segundo número >')
r=n1+n2
print('Concatenando String')
print('O Resultado é {}'.format(r))
r=int(n1)+int(n2)
m= int(n1)/int(n2)
print('Convertendo  String')
print('O Resultado soma é {} e divisao {:.2f}'.format(r,m))

z = input('Digite algo: ')

# Faz a análise
print("== Desafio 004 ==")
if z.isnumeric() == True:
    a = ('É numérico')                #0
else:
    a = ('Não é númerico')
if z.isalpha() == True:
    b = ('É alpha')                   #1
else:
    b = ('Não é alpha')
if z.isalnum() == True:
    c = ('É alpha numérico')          #2
else:
    c = ('Não é alpha numérico')
if z.isdecimal() == True:
    d = ('É decimal')                 #3
else:
    d = ('Não é decimal')
if z.isupper() == True:
    e = ('Está em maiúsculo')         #4
else:
    e = ('Não está em maiúsculo')
if z.islower() == True:
    f = ('Está em minúsculo')         #5
else:
    f = ('Não está em minúsculo')

# Mostra o resultado da análise

print('O que você digitou {0} \n{1} \n{2} \n{3} \n{4} \ne {5}'.format(a, b, c, d, e, f))  # '\n' pula linha
print(' = '*20)
desa ='desafio 05'
print(' {:=^30} '.format(desa))
n3=int(input('Um numero'))
print('o numero {}, seu Antecessor {} seu sucessor {}'.format(n3,(n3-1),(n3+1) ))


print('====== DESAFIO 06 ======')
n4=int(input('outro numero '))
print('o numero {}, seu dobro {} , seu triplo {} sua potencia {} e sua raiz {:.2F}'.format(n4,(n4*2),(n4*3),(n4**2),(n4**1/2)))



print('====== DESAFIO 07 ======')
n5=int(input('nota  1 '))
n6=int(input('nota 2'))
print('a media das notas {:.2f}'.format((n5+n6)/2))

print('====== DESAFIO 08 ======')
n7=int(input('metragem '))
print('{} metros equivale {} centrimetros {} milimetros'.format(n7,(n7*100),(n7*1000)))

print('====== DESAFIO 09 ======')
n8=int(input('a tabuada vai ser  :'))
i=0
for i in range(11):
    print('tabuada {} X {} = {}'.format(n8,i,(n8*i)))
    i=i+1


print('====== DESAFIO 10 ======')

n9=int(input('quando na carteira : '))
print('vc tem R$ {} comprar USS {:.2f} '.format(n9,(n9/3.27)))

print('====== DESAFIO 11 ======')
n10=int(input('altura parede : '))
n11=int(input('largura parede : '))
area=n10*n11
tinta=area/2
print('a area é {} vai precisar {} tinta'.format(area,tinta))

print('====== DESAFIO 12 ======')

n12=int(input('preço do produto : '))
desconto= n12 - (n12*0.05)
print('produto era R$ {} com desconto R${}'.format(n12,desconto))

print('====== DESAFIO 13 ======')
n13=int(input('salario : '))
salnovo= n13 + (n13*0.15)
print('salario era R$ {} com aumento R${}'.format(n13,salnovo))










