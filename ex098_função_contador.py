#Exercício Python 098: Faça um programa que tenha uma função chamada contador(),
# que receba três parâmetros: início, fim e passo. Seu programa tem que realizar
# três contagens através da função criada:

#a) de 1 até 10, de 1 em 1
#b) de 10 até 0, de 2 em 2
#c) uma contagem personalizada

from time import sleep

def contador (i, f, p):
    print(f'Contagem de {i} a {f} de {p} em {p}. ')
    sleep(2)
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ')
            cont += p
            sleep(0.5)
        print("FIM!")

    elif f < i:
        cont = i
        while cont >= f:
            print(f'{cont}', end=" ")
            cont -= p
            sleep(0.5)
        print("FIM!")

contador(100, 10, 10)
sleep(1)
contador(10, 1, 2)
sleep(1)
contador(1, 10, 1)
sleep(1)
print("Agora personalize sua contagem: ")
sleep(0.5)
inicio = int(input("Digite o número inicial: "))
fim = int(input("Digite o número final: "))
passo = int(input("Doigite o passo: "))

contador(inicio, fim, passo)