'''Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.'''

cobertura_tinta = 3
tamanho_lata = 18
preco_lata = 80.00

tamanho_area_a_ser_pintada = float(input('Tamanho da área a ser pintada: '))

litros = tamanho_area_a_ser_pintada / cobertura_tinta
latas_inteiras = int(litros / tamanho_lata)

if litros % tamanho_lata != 0:
    latas_inteiras += 1

valor_total = latas_inteiras * preco_lata

print(f'Quantidade de litros de tinta necessários: {litros:.2f}')
print(f'Quantidade de latas de tinta necessárias: {latas_inteiras}')
print(f'Valor total da compra: R$ {valor_total:.2f}')
