from random import choice

aluno1 = str(input('Qual é o primeiro aluno? '))
aluno2 = str(input('Qual é o segundo aluno? '))
aluno3 = str(input('Qual é o terceiro aluno? '))
aluno4 = str(input('Qual é o quarto aluno? '))

lista = [aluno1, aluno2, aluno3, aluno4]

escolhido = choice(lista)

print(f'O aluno sorteado foi {escolhido}.')
