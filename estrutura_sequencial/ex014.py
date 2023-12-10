'''João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.'''

peso_de_peixes = float(input('Peso de peixes kg: '))
peso_permitido = 50
excesso = peso_de_peixes - peso_permitido
multa = excesso * 4

print(f'Você pescou {peso_de_peixes} kg de peixe, dos {peso_permitido}kg permitido ')

if peso_de_peixes <= peso_permitido:
    print('Peso dentro do limite permitido. ')

else:

    print(f'O peso foi excedio em {excesso:.1f}kg, e será aplicado uma multa de R$ {multa:.2f}')