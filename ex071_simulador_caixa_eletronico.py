
print('Bem vindo ao banco CEV!\n')


valorSaque = int(input('Digite o valor que quer sacar: R$\n'))

for nota in [50, 20, 10, 1]:
    quantidade = valorSaque // nota
    valorSaque = valorSaque % nota
    if quantidade > 0:
        print(f'{quantidade} notas de R$ {nota}')