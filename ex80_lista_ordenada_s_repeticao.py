#Exercício Python 080: Crie um programa onde o usuário possa
#digitar cinco valores numéricos e cadastre-os em uma lista,
#já na posição correta de inserção (sem usar o sort()).
#No final, mostre a lista ordenada na tela.

lista = []

print("Vamos começar uma lista de 5 números!\n")

for c in range(0,5):
    n = (int(input(f"Digite o número {c}: ")))
    if n not in lista:
        lista.append(n)
print(f"Você criou uma lista com {len(lista)} e os valores são {lista}.\n")

print('FIM')
