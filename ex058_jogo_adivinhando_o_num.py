#adivinhando o numero que o computador sorteou

from random import randint
num = randint(1, 10)
n = int(input("Qual número você acha que eu adivinhei? "))
t = 1
while n != num:
    n = int(input("Errrou! Tente outra vez: "))
    t += 1
print("Isso, eu escolhi o número {}! Você descobriu em {} tentativas.".format(num, t))