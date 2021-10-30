print("Vamos iniciar uma lista de cadastro de pessoas:\n")
continuar = 's'
pessoas = list()
cont_pessoas = 0
idades = list()
mulheres = 0
somaidades = 0
mediaidades = 0

while continuar in 'Ss':
    nome = str(input("Nome: "))
    cont_pessoas += 1
    pessoas.append(nome[:])
    sexo = str(input(f"Sexo de {nome} "))
    if sexo not in 'FfMm':
        print("erro: por favor digite F ou M: ")
        sexo = str(input(f"Sexo de {nome} "))
    if sexo in 'Ff':
        mulheres += 1
    idade = int(input(f"Idade de {nome}: \n"))
    idades.append(idade)
    somaidades += idade
    continuar = str(input("Quer cadastrar mais pessoas? [S/N]:"))
print(f'Ao todo temos {cont_pessoas} pessoas cadastradas')
mediaidades = somaidades/cont_pessoas
print(f'A média de idades é {mediaidades}.')
print(f'O número de mulheres cadastradas é {mulheres}.')

