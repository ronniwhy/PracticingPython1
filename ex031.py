distancia = float(input('Qual é a distância de sua viagem? (Em Km) '))

if distancia <= 200:
    passagem = distancia*0.50
    print(f'A passagem vai custar: R${passagem:.2f}')
else:
    passagem = distancia*0.45
    print(f'A passagem vai custar R${passagem:.2f}')
