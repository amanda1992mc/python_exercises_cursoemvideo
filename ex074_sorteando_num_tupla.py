# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint

tupla = (randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9))

print(f"Os números sorteados foram {tupla}.")
print(f"O maior valor sorteado foi {max(tupla)}.")
print(f"O menor valor sorteado foi {min(tupla)}.")

