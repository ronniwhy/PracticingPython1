salario = float(input('Digite o valor de seu salário: '))

if salario > 1250:
    salario = (salario * 10/100) + salario
    print(f'O seu salário vale, agora, {salario:.2f}.')
if salario <= 1250:
    salario = (salario * 15/100) + salario
    print(f'O seu salário vale, agora, {salario:.2f}.')
