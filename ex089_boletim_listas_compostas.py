# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo
# em uma lista composta. No final, mostre um boletim contendo a média de cada um
# e permita que o usuário possa mostrar as notas de cada aluno individualmente.
ficha = []

while True:
    nome = str(input("Digite o nome do aluno: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2)/2
    ficha.append([nome, [nota1, nota2], media])
    continuar = str(input("Quer continuar? [S/N] ")).upper()
    if continuar not in 'NS':
        continuar = str(input("Não entendi. Quer continuar? [S/N] ")).upper()
    if continuar in 'N':
        break
print(f'{"No":<4}{"Nome":<10}{"MÉDIA":>8}')
print("-"*25)
for i, a in enumerate(ficha):
    print(f"{i:<4}{a[0]:<10}{a[2]:>8.1f}")
print("-"*25)
while True:
    notas = str(input("Você quer ver as notas de algum aluno? [S/N] ")).upper()
    if notas in 'S':
        aluno = (int(input("Digite o No do aluno que você quer ver as notas: ")))
        print(f"As notas de {ficha[aluno][0]} são {ficha[aluno][1]}")
    if notas in 'N':
        break
print("Finalizado")


