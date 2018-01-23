
r1 = float(input('valor da reta 1 '))
r2 = float(input('valor da reta 2 '))
r3 = float(input('valor da reta 3 '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('1 forma um triangulo')
else:
    print('1 nao forma triangulo')

if abs(r1 - r3) < r2 and r2 < r1 + r3 or abs(r2 - r3) < r1 and r1 < r2 + r3 or abs(r1 - r2) < r3 and r3 < r1 + r2:
    print('2 forma um triangulo')
else:
    print('2 nao forma triangulo')

if abs(r1 - r3) < r2 < r1 + r3 or abs(r2 - r3) < r1 < r2 + r3 or abs(r1 - r2) < r3 < r1 + r2:
    print('3 forma um triangulo')
else:
    print('3 nao forma triangulo')
