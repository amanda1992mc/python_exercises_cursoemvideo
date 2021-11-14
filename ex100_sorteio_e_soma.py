# Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções
# chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los
# dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados
# pela função anterior.
import random

def sorteia(lista):
    for cont in range(0,5):
        lista.append(random.randint(1,10))

números = list()
sorteia(números)
print(números)

def somapar(lista):
    soma = 0
    for cont in lista:
        if cont % 2 == 0:
            soma += cont
    print(soma)


print(somapar(números))




