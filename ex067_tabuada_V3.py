#tabuada V3

m = 1
r = 's'

while r == 's':
    n = int(input("Digite um número para ver sua tabuada até 10: "))
    m = 0
    while m <= 10:
        print(f'{n} x {m} = {(n*m)}')
        m += 1
    r = str(input('Pronto! Quer ver mais alguma tabuada? Digite [s] ou [n]: '))

print("Programa finalizado pelo usuário.")
