# Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

print('Vamos cadastrar pessoas: \n')

maior18 = 0
homens = 0
mulheresmenos20 = 0

while True:
    while True:
        sexo = str(input("Você quer cadastrar um homem [H] ou uma mulher [M]? ")).upper()
        if sexo != 'H' and sexo != 'M':
            print('Não entendi. Digite novamente.')
        if sexo == 'H':
            homens += 1
            break
        elif sexo == 'M':
            break

    while True:
        idade = int(input("E qual a idade dessa pessoa? "))
        if type(idade) != int:
            print('Não entendi. Digite novamente.')
        if idade <= 20 and sexo == "M":
            mulheresmenos20 += 1
            break
        elif idade >= 18:
            maior18 += 1
            break

    while True:
        cont = str(input("Ok, essa pessoa foi cadastrada. Você quer cadastrar mais alguém?\nDigite [S] ou [N]:\n")).upper()
        if cont != 'S' and cont != 'N':
            print('Não entendi. Digite novamente.')
        elif cont == 'S':
            break
        if cont == 'N':
            break
    if cont == 'N':
        break
print(f'Você cadastrou {maior18} pessoa com mais de 18 anos, {mulheresmenos20} mulher(es) com menos de 20 anos e {homens} homens.')
