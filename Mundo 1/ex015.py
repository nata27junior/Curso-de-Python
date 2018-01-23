dia = int(input('quantos dias '))
km = float(input('quantos km '))

custo = (km * 0.15) + (dia * 60)

print('{} dias {} KM custo R$ {:.2f}'.format(dia, km, custo))
