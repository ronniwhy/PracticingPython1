from math import sin, cos, tan, radians, degrees

num1 = float(input('Digite um ângulo '))

seno = sin(radians(num1))
cosseno = cos(radians(num1))
tangente = tan(radians(num1))

print(f'Seno de {num1}º: {seno:.2f}\n'
      f'Cosseno de {num1}º: {cosseno:.2f}\n'
      f'Tangente de {num1}º: {tangente:.2f}')
