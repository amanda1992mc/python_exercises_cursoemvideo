#progressão aritmética

n = int(input("Digite um número para ver sua progressão aritmética: "))
razão = int(input("Digite a razão: "))

for c in range(10):
    n += razão
    print(n, end=' - ')
print("FIM")