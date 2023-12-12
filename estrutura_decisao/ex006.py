"""Faça um Programa que leia três números e mostre o maior deles"""

numero_1 = int(input('Digite um número: '))
numero_2 = int(input('Digite outro número: '))
numero_3 = int(input('Digite mais um número: '))

print(f'O números digitados foram {numero_1}, {numero_2} e {numero_3}')

if numero_1 > numero_2 and numero_1 > numero_3:
    print(f'{numero_1} é maior ')
elif numero_2 > numero_1 and numero_2 > numero_3:
    print(f'{numero_2} é maior ')
else:
    print(f'{numero_3} é maior ')

