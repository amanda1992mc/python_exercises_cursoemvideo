# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores
# numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro,
# ele não será adicionado. No final, serão exibidos todos os valores únicos
# digitados, em ordem crescente.


lista = []
user = 's'
print("Vamos começar uma lista de números!\n")
while user == 's':
    num = int(input("Digite um número: "))
    if num not in lista:
        lista.append(num)
    user = str(input("Quer continuar? Digite s ou n: "))
print(f"Você criou uma lista com os valores {lista}.\n")
print('FIM')



