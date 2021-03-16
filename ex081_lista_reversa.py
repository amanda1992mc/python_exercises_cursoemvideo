# Exercício Python 081: Crie um programa que vai ler vários números e
# colocar em uma lista.
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []

print("Vamos começar uma lista de números!\n")

while True:
    lista.append(int(input("Digite um número: ")))
    user = str(input("Quer continuar? Digite s ou n: "))
    if user in 'Nn':
        break
lista.sort(reverse=True)
print(f"Você criou uma lista com {len(lista)} e os valores são {lista}.\n")
if 5 in lista:
    print("O numero 5 está na lista.")
print('FIM')


