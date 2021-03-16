#maior e menor peso da sequência

pesos = []
c = 0
for c in range(1,6):
    pesos = float(input("Digite o peso: "))
    pesos += pesos
    c += 1
pesos.sort()
print('O maior peso é {} e o menor é {}.'.format(pesos[0], pesos[-1]))