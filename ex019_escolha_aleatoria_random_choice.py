##biblioteca random: sorteio - escolha aleatoria
'''Sorteio de aluno para apagar a lousa'''
'''Rando = aleatorio | choice = escolher 1'''

import random

a1 = input("Escreva o nome do primeiro aluno: ")
a2 = input("Escreva o nome do segundo aluno: ")
a3 = input("Escreva o nome do terceiro aluno: ")
a4 = input("Escreva o nome do quarto aluno: ")

lista = [a1,a2,a3,a4]
escolha = random.choice(lista)
print("O aluno escolhido para apagar a lousa é {}.".format(escolha))
