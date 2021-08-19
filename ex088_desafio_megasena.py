#088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60
# para cada jogo, cadastrando tudo em uma lista composta.

from random import randint

print('Bem vindo a jogo da mega sena! Vou sugerir números aleatórios para você.\n')
jogos = int(input("Quantos jogos da megasena você quer fazer? \n"))

lista = []
cont_jogos = 1
while cont_jogos <= jogos:
    cont_numeros = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont_numeros += 1
        if cont_numeros > 6:
            break
    cont_jogos += 1
    lista.sort()
    print(f'Os números sorteados para o jogo {cont_jogos - 1} foram {lista}. ')
    lista.clear()
print('\nBoa sorte!')