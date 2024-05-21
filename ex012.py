produto = float(input('Digite o valor do produto: '))
desconto = float(input('Digite o valor do desconto: '))

descontoproduto = produto - ((produto * desconto) / 100)

print(f'O produto que custava R${produto:.2f} agora custa R${descontoproduto:.2f}.')
