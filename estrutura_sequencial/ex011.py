'''Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
a) o produto do dobro do primeiro com metade do segundo .
b) a soma do triplo do primeiro com o terceiro.
c) o terceiro elevado ao cubo.'''

primeiro_inteiro = int(input('Primeiro número: '))
segundo_inteiro = int(input('Segundo número: '))
terceiro_real = float(input('Número real: '))

print('a) o produto do dobro do primeiro com metade do segundo. ', (primeiro_inteiro * 2) * (segundo_inteiro / 2) )
print('b) a soma do triplo do primeiro com o terceiro. ', (primeiro_inteiro * 3) + terceiro_real)
print('c) o terceiro elevado ao cubo. ', terceiro_real ** 3)

