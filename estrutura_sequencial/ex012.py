'''Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58'''

altura = float(input('Altura: '))
peso_ideal = (72.7 * altura) - 58

print(f'Para uma pessoa de {altura}m de altura o peso ideal é de {peso_ideal:.2f}')

