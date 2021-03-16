#calculo de maioridade

from datetime import date
hoje = date.today().year
menor = 0
maior = 0
for pessoa in range(1,8):
    ano = int(input("Digite o ano de nascimento da pessoa: "))
    nome = str(input("Digite o nome da pessoa: "))
    if ano < 2000 and ano < 1900 and ano > 19:
        ano += 1900
    elif 0 < ano < 19:
        ano += 2000
    idade = hoje - ano
    if idade < 18:
        print('A {}ª pessoa, {}, é menor de idade. Ele(a) tem {} anos'.format(pessoa, nome, idade))
        menor += 1
    else:
        print('A {}ª pessoa, {}, é maior de idade. Ele(a) tem {} anos'.format(pessoa, nome, idade))
        maior += 1
print("No total tivemos {} pessoas de maior e {} menores de idade.".format(maior, menor))