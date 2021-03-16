#Desenvolva um programa que leia quatro valores pelo teclado e
#guarde-os em uma tupla. No final, mostre:

#A) Quantas vezes apareceu o valor 9.
#) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

print("Para esse programa funcionar, você precisar digitar 4 números, um por vez.\n")
pares = []

tuple1 = (int(input("Digite o primeiro número: ")),
          int(input("Digite o segundo número: ")),
          int(input("Digite o terceiro número: ")),
          int(input("Digite o quarto e último número: ")))
if 9 in tuple1:
    print(f'O valor 9 apareceu {tuple1.count(9)} vezes.')
if 3 in tuple1:
    print(f'O primeiro registro do número 3 foi na posição {tuple1.index(3)}.')
for n in tuple1:
    if n % 2 == 0:
        pares.append(n)
print(f'Os números pares digitados foram {pares}')
