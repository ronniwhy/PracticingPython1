metros = float(input("Digite um número em metros: "))

km = metros / 1000
hm = metros / 100
dm = metros / 10
cm = metros * 100
mm = metros * 1000

print(f'{km:.2f}km')
print(f'{hm:.2f}hm')
print(f'{dm:.2f}dm')
print(f'{cm:.2f}cm')
print(f'{mm:.2f}mm')