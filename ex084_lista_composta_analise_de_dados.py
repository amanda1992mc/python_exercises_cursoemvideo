listafinal = []
pessoas = []
cont = 'Ss'
n = 0

print('Digite o nome de uma pessoa e seu peso.\n')
while cont in 'Ss':
    nome = (input("Digite o nome da pessoa: "))
    pessoas.append(nome[:])
    peso = (input("Agora digite o peso da pessoa: "))
    pessoas.append(peso[:])
    listafinal.append(pessoas[:])
    listafinal.sort()
    n += 0
    pessoas.clear()
    cont = input('Você quer continuar? [S/N] ')
    while cont not in 'Ss' and cont not in 'Nn':
        cont = input('Não entendi. Você quer continuar? [S/N] ')
    if cont in 'Nn':
        break
print(f'Foram incluidas {n} pessoas na lista.')
print(listafinal)
print(f"A pessoa mais pesada é {listafinal[-1]}")