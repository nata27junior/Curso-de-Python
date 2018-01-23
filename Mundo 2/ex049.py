num = int(input('tabuada do :'))
print('-'*15)
for i in range(11):
    print('| {} X {:2} = {:2} |'.format(num, i, num * i))

print('-'*15)
num = 12345679
print('-'*15)
for i in range(11):
    print('| {} X {:2} = {:2} |'.format(num, i*9, num *(i*9) ))

print('-'*15)