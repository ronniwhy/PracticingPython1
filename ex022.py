nome = str(input('Digite seu nome completo: '))

print(nome.upper())
print(nome.lower())
print(len(nome.replace(' ', '')))
nome = nome.split()
nome = nome[0]
print(len(nome))
