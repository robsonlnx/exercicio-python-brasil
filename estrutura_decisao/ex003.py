"""Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido. """

sexo = input('Digite uma letra. [F] - Feminino, [M] - Masculino: ')

if sexo == 'F'.lower():
    print('Feminino')

elif sexo == 'M'.lower():
    print('Masculino')

else:
    print('Sexo inválido')
