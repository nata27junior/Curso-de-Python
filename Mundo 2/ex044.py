print('{:=^40}'.format(' Casas Cabia '))  # ^centralizado entre 40 espaços
print('''Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros''')
preco = float(input('preço do produto'))
print('''
[1] à vista dinheiro/cheque
[2] à vista no cartão
[3] em até 2x no cartão
[4] 3x ou mais no cartão''')
escolha = int(input('Qual é a opção? '))

if escolha == 1:
    pagamento = preco - (preco * 0.1)
    print('o pagamento a vista o valor {}'.format(pagamento))
elif escolha == 2:
    pagamento = preco - (preco * 0.05)
    print('o pagamento a vista no cartao o valor {}'.format(pagamento))
elif escolha == 3:
    parcela = preco / 2
    print('sua compra sera parcelada em 2x no cartao o valor {}'.format(parcela))
elif escolha == 4:
    pagamento = preco + (preco * 0.2)
    totalparc = int(input('Quantas parcelas?'))
    parcela = pagamento / totalparc
    print('sua compra sera parcelada em {}X de R${:.2f} com Juros'.format(totalparc,parcela))
else:
    pagamento=preco
    print('opçao invalida')
print('sua compra de R$ {:.2f} vai custar R$ {:.2f} no final'.format(preco, pagamento))
