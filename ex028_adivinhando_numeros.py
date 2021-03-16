#Adivinhar número que o computador escolheu
#computador pensa num numero de 0 a 5 e o jogador(usuário) tem que adivinhar

from random import randint
computador = randint(0,5)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar!")
jogador = int(input("Digite o que você acha que o computador pensou: "))
if jogador == computador:
    print("Parabéns! Você acertou!")
else:
    print("Na verdade eu pensei no número {}". format(computador))
