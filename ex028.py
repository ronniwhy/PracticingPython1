from random import randint
from time import sleep

pensar = randint(0, 5)

print(pensar)

print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
adivinhar = int(input('Digite um número: '))

print('Processando...')
sleep(3)
if adivinhar == pensar:
    print('Parabéns! Você adivinhou o que pensei.')
else:
    print(f'Errou! Eu pensei no {pensar}, não no {adivinhar}.')
