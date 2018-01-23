casa = float(input('qual o valor da casa'))
salario = float(input('qual o seu salario'))
anos = int(input('quantos anos vai pagar'))
meses = anos * 12
prestacao = casa / meses
valor = casa/meses

salarionovo = salario * 0.30

print('Para pagar uma casa de R${:.2f} em  {} anos '.format(casa, anos), end='')
print('a prestaçao sera de R${:.2f}'.format(prestacao))

if prestacao <= salarionovo:
    print('parabens voce pode pagar')
else :
    print('infelizmente nao pode ')