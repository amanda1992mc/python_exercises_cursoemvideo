#biblioteca random: embaralhar e sortear ordem de lista
'''Sorteio de ordem para apresentar trabalho'''
'''Rando = aleatorio | shuffle = embaralhar'''

import random
n1 = input("Digite o nome do aluno: ")
n2 = input("Digite o nome do outro aluno: ")
n3 = input("Digite o nome do outro aluno: ")
n4 = input("Digite o nome do outro aluno: ")
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print("A ordem de apresentação será a seguinte: {}".format(lista))

'''O método shuffle() embaralha a lista e então retorna um valor vazio, ou seja, esse 
none é o valor vazio, por isso se você der print(shuffle(x)) o valor retornado será 
none. Logo, o correto é primeiro embaralhar a lista e apenas após isso printar ela.'''