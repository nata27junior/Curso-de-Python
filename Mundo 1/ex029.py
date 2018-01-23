#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h. Mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$ 7,00 por cada km acima do limite.
'''

velocidade = float(input('Velocidade do carro: '))

if velocidade > 80:
    print('Você foi MULTADO!')
    calculo = velocidade - 80
    print('Custo da multa: R${:.2f}'.format(calculo*7.00))
else:
    print('O Veiculo esta no limite da velocidade')