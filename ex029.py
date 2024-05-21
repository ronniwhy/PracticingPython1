carro = float(input('Digite a velocidade do carro (em Km/h): '))

if carro >= 80:
    excedente = (carro-80)*7
    print(f'''\033[31mVelocidade máxima ultrapassada!
A multa vai custar\033[0m \033[33mR$7,00\033[0m \033[31mpor cada Km acima do limite.
Realizando o cálculo de velocidade excedente...
Você deve pagar:\033[0m \033[33mR${excedente:.2f}\033[0m''')
else:
    print('\033[32mParabéns! Continue seguindo as leis de trânsito.\033[0m')
