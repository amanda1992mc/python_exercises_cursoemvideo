#jokenpo


from time import sleep
from random import randint
comp = randint(1,3)

print('''
Vamos jogar jokenpo!\n
[1] papel
[2] pedra
[3] tesoura\n''')
sleep(1)
user = int(input("Escolha a sua jogada e aperte enter: "))

sleep(3)

print("O compoutador escolheu {}.".format(comp))

sleep(1)

if user == comp:
    print("Empate! Tente novamente.")
elif user == 1 and comp == 2:
    print("Papel vence pedra: Você venceu!")
elif user == 2 and comp == 3:
    print("Pedra quebra tesoura: Você venceu!")
elif user == 3 and comp == 1:
    print("Tesoura corta papel: Você venceu!")
elif user == 1 and comp == 3:
    print("Tesoura corta papel: você perdeu!")
elif user == 2 and comp == 1:
    print("Papel embrulha a pedra: você perdeu!")
elif user == 3 and comp == 2:
    print("Pedra quebra tesoura: você perdeu!")
else: print("Dígito inválido, tente novamente.")




