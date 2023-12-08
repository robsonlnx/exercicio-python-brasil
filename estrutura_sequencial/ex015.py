'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.'''

valor_hora = float(input('Valor da hora trabalhada: R$ '))
horas_trabalhadas = int(input('Horas trabalhadas: '))
salario_bruto = horas_trabalhadas * valor_hora
inss = (salario_bruto * 8 / 100)
sindicato = (salario_bruto * 5 / 100)
ir = (salario_bruto * 11 / 100)
salario_liquido = salario_bruto - inss - sindicato - ir

print(f'+ Salário Bruto:............... R$ {salario_bruto:.2f}')
print(f'- IR (11%):.................... R$ {ir:.2f}')
print(f'- INSS (8%):................... R$ {inss:.2f}')
print(f'- Sindicato ( 5%):............. R$ {sindicato:.2f}')
print(f'= Salário Liquido:............. R$ {salario_liquido:.2f}')

