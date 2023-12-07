'''Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.'''

temperatura_celsius =  float(input('Qual temperatura deseja converter: '))
graus_fahrenheit = (temperatura_celsius * 9 / 5) + 32

print(f'A temperatura de {temperatura_celsius:.2f} convertida para graus fahrenheit é igual a {graus_fahrenheit:.2f}')

