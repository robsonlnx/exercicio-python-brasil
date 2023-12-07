"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês."""

valor_hora = float(input('Quanto você ganha por hora? R$ '))
horas_trabalhadas = int(input('Quantas horas você trabalhou esse mês? '))

salario_do_mes = horas_trabalhadas * valor_hora

print(f'Você trabalhou {horas_trabalhadas} horas esse mês é seu salário foi de R$ {salario_do_mes:.2f}')

