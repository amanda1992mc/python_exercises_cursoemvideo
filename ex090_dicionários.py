#Exercício Python 090: Faça um programa que leia nome e média de um aluno,
# guardando também a situação em um dicionário. No final, mostre o conteúdo da
# estrutura na tela.


aluno = dict()

aluno['nome'] = str(input('Digite o nome do aluno: '))
aluno['nota1'] = float(input(f'Digite a 1ª nota de  {aluno["nome"]}: '))
n1 = aluno['nota1']
aluno['nota2'] = float(input('Digite a 2 nota do aluno: '))
n2 = aluno['nota2']
aluno['media'] = float(n1 + n2) / 2
if aluno['media'] >= 6:
    aluno['situação'] = 'aprovado'
elif aluno['media'] < 6:
    aluno['situação'] = 'reprovado'

print(aluno)






