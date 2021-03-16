print("=-=-=-=-=-=  Gerador de Progressão Aritmética  =-=-=-=-=-=-=-=\n")

n = int(input("Digite um número para ver sua progressão aritmética: "))
razao = int(input("Digite a razão: "))
c = 0
f = 0
while c <= 10:
    n += razao
    c += 1
    print(n, end=' - ')

print("Esses são os 10 primeiros termos.")
t = int(input(" \nQuantos mais você quer ver? "))
while t > 0:
    for e in range(t):
        n += razao
        print(n, end=' - ')
        f += 1
    print("Esses são os {} próximos.".format(t))
    t = int(input("\nQuantos mais você quer ver? "))
print("Foram mostrados {} termos. \nFim!".format(f + 10))
