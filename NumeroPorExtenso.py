'''
Número por extenso. Escreva um programa que solicite ao usuário a digitação de um número até 99 e
imprima-o na tela por extenso.
'''

from num2words import num2words
numero = input('Digite um número: ')
numero = numero.replace(',', '.') 
numero = float(numero)

inteiro, decimal = str(numero).split('.')
num_ptbr = num2words(inteiro, lang='pt_BR')

if decimal and int(decimal) > 0: 
    decimal = decimal.ljust(2, '0')
    num_ptbr += ' vírgula ' + num2words(decimal, lang='pt_BR') + ' centavos'

print(f'\nNúmero por extenso: {num_ptbr.capitalize()}')
print()
