real = float(input('Digite o seu saldo em R$: '))

dolaremreal = 5.16  # Cotação atual
real = real / dolaremreal
print(f'Se você tem R${real:.2f}, você pode comprar US${dolaremreal:.2f}.')
