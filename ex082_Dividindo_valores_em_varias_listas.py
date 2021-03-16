# Exercício Python 082: Crie um programa que vai ler vários números e colocar em
# uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores
# pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo
# das três listas geradas.

lista1 = []
listapar = []
listaimpar = []

print("Vamos cadastrar números e separa-los em listas de par e ímpar:\n")

while True:
    n = int(input("Digite um número: "))
    lista1.append(n)
    if n % 2 == 0:
        listapar.append(n)
    else:
        listaimpar.append(n)
    user = str(input("Deseja continuar? [S/N] "))
    if user in 'Nn':
        break
print(f'O total de números digitados foi {len(lista1)} e os números foram {lista1}.')
print(f'Os pares são {listapar}.')
print(f'Os ímpares são {listaimpar}.')
