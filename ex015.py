km = float(input('Digite a quantidade de kM/h percorridos: '))
dias = float(input('Digite a quantidade de dias que o carro foi alugado: '))

calc = (km * 0.15) + (dias * 60)

print(f'O total a pagar é de R${calc:.2f}')
