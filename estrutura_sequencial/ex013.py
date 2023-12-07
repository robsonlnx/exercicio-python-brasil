'''Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7'''

altura = float(input('Altura: '))
peso_ideal_homem = (72.7 * altura) - 58
peso_ideal_mulher = (62.1 * altura) - 44.7

print(f'Para um homem de {altura}m de altura seu peso ideal é de {peso_ideal_homem:.2f}')
print(f'Para uma mulher de {altura}m de altura seu peso ideal é de {peso_ideal_mulher:.2f}')

