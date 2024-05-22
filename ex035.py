segmento1 = float(input('Digite o segmento 1: '))
segmento2 = float(input('Digite o segmento 2: '))
segmento3 = float(input('Digite o segmento 3: '))

if segmento1 < segmento2 + segmento3 and segmento2 < segmento1 + segmento3 and segmento3 < segmento1 + segmento2:
    print('Um triângulo pode ser feito.')
else:
    print('Um triângulo não pode ser feito.')
