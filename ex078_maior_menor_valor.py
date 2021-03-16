# Exercício Python 078: Faça um programa que leia 5 valores numéricos e
# guarde-os em uma lista. No final, mostre qual foi o maior e o
# menor valor digitado e as suas respectivas posições na lista.

lista = []
for c in range(0,5):
    lista.append(int(input("Digite um número para a lista: ")))
print(f"Você digitou {lista}")
print(f"O maior valor da lista digitada é {max(lista)} na posição {lista.index(max(lista))+1}")
print(f"O menor valor da lista digitada é {min(lista)} na posição {lista.index(min(lista))+1}")

