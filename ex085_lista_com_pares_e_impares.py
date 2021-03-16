print('Vamos digitar 7 valores numericos, separar em pares e ímpares.\n')

listafinal = []
pares = []
impares = []

for n in range(1, 8):
    valor = int(input(f"Digite o {n}º valor: "))
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
pares.sort()
impares.sort()
listafinal.append(pares)
listafinal.append(impares)
listafinal.sort()

print(f'Os números ímpares são {impares}')
print(f'Os números pares são {pares}')
print(f"Os valores digitados foram {listafinal}")
