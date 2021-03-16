#progressão artimética V2

print("Gerador de Progressão Aritmética")

n = int(input("Digite um número para ver sua progressão aritmética: "))
razão = int(input("Digite a razão: "))
c = 0

while c <= 10:
    n += razão
    c += 1
    print(n, end=' - ')
print("FIM")
