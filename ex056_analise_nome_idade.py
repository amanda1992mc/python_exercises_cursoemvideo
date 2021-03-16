#analise de idade, peso e nome de pessoas

idade = 0
somaidade = 0
media = 0
for c in range(1,3):
    name = str(input("Digite o nome da pessoa: "))
    idade = int(input("Digite a idade da pessoa: "))
    sexo = str(input("Digite o sexo da pessoa: [F] ou [M]? ")).strip().upper().split()[0]
    somaidade += idade
    media = somaidade / c
print("A média de idade é {}.".format(media))


