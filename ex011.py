largparede = float(input('Digite o valor da largura da parede em metros: '))
altparede = float(input('Digite o valor da altura da parede em metros: '))

area = largparede * altparede
tinta = area/2

print(f'A dimensão da parede é de {largparede}x{altparede}.')
print(f'A área da parede é de {area:.3f}m².')
print(f'A quantidade de tinta necessária é {tinta:.4f}l de tinta.')
