from math import hypot
from emoji import emojize

num1 = float(input('Digite o valor do cateto 1: '))
num2 = float(input('Digite o valor do cateto 2: '))

hipotenusa = hypot(num1, num2)

print(f'Encontrei essa tal {hipotenusa:.2f}! {emojize('😎')}')
