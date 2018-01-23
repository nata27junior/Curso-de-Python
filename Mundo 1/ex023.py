num=input('digite um numero 0 a 9999 ')

num2=int(num)
uni = num2 //1 % 10
dez = (num2 //10)%10
cen= num2 //100 %10
mi=num2 // 1000 % 10
# print('unidade {}'.format(num[3]))
# print('dezena {}'.format(num[2]))
# print('centena {}'.format(num[1]))
# print('milhar {}'.format(num[0]))

print('mat unidade  {}'.format(uni))
print('dezena {}'.format(dez))
print('centena {}'.format(cen))
print('milhar {}'.format(mi))