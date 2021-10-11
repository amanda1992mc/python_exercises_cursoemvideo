#Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira
#de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for
#diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
#Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime


dados = dict()
dados['nome'] = str(input("Digite o nome da pessoa: "))
nasc = int(input("Digite o ano de nascimento da pessoa: "))
dados['idade'] = (datetime.now().year - nasc)
trabalho = int(input(f"Digite o ano em que começou a trabalhar: "))
dados['ctps'] = int(input("Digite o número da ctps da pessoa (ou 0 se não houver): "))
if dados['ctps'] != 0:
    dados['contratação:'] = int(input("Ano de contratação: "))
    dados['salario'] = int(input("Salário atual: "))
    dados['aposentadoria'] = (dados['contratação:'] + 35) - datetime.now().year
else:
    for k,v in dados.items():
        print(f"O {k} é {v}.")
for k,v in dados.items():
    print(f'O {k} é {v}.')
