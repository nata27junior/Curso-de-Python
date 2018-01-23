dis = float(input('digite a distancia '))
if dis <= 200:
    pre = dis * 0.5
    print('preço valor R${} pela distancia {}KM '.format(pre, dis))
else:
    pre = dis * 0.45
    print('preço valor R${} pela distancia {}Km '.format(pre, dis))
    print('\033[35m' + 'E o preço da sua passagem será de {:.2f}'.format(pre))
    print('\033[32m' + 'Isto é verde')