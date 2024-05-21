salario = float(input('Digite o seu salário: '))
aumentosalarial = float(input('Digite a porcentagem de aumento salarial: '))

salarioajustado = salario + ((salario * aumentosalarial) / 100)

print(f'O aumento foi de {aumentosalarial}%.')
print(f'O seu salário agora é de {salarioajustado}.')
