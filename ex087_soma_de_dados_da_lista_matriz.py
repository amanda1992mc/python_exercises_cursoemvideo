# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0,0,0], [0,0,0], [0,0,0]]
pares = 0
somacoluna3 = 0
somalinha2 = 0

for l in range (0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para a posição {l}:{c}: '))
        somalinha2 += matriz[1][c]
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
    somacoluna3 += matriz[l][2]


print(matriz[0], end ='\n')
print(matriz[1], end ='\n')
print(matriz[2], end ='\n')

print(f'A soma dos valores pares é {pares}.')
print(f'A soma da última coluna é {somacoluna3}')
print(f'A soma da segunda linha é {somalinha2}')

