"""Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:

    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    A mensagem "Reprovado", se a média for menor do que sete;
    A mensagem "Aprovado com Distinção", se a média for igual a dez. """


primeira_nota = float(input('Primeira nota: '))
segunda_nota = float(input('Segunda nota: '))
media = (primeira_nota + segunda_nota) / 2

print(f'Média obtida é igual a {media}')

if media >= 7 and media < 10:
    print('Aluno APROVADO')
elif media < 7:
    print('Aluno REPROVADO')
elif media == 10:
    print('Aluno APROVADO COM DISTINÇÃO')

