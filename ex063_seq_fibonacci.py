#sequencia de fibonacci
#0 1 1 2 3 5 8

n = int(input("Quantos termos você quer ver numa sequência de Fibonacci? "))

lista = [0,1]

n -= 2
c = 0

while c < n:
    n1 = lista[-1]
    n2 = lista[-2]
    n3 = n1 + n2
    lista.append(n3)
    c += 1

print(f'A sequência de Fibonacci com {n+2} dígitos é {lista}.')

