from random import randint
import sys

pontuacaouser = 0
pontuacaomaquina = 0


jogo = input("Vamos brincar de par ou impar? Digite sim [s] ou não [n]. ").lower()
if jogo == 'n':
    print('Programa encerrado.')
    sys.exit(0)
elif jogo != 's':
    print("Resposta Inválida.")
    jogo = input("Vamos brincar de par ou impar? Digite sim [s] ou não [n]. ").lower()
elif jogo == 's':
    while True:
        user = str(input("Você prefere ser ímpar [digite i] ou par [digite p]? "))
        if user != 'p' and user != 'i':
            print("Resposta inválida.")
            user = str(input("Você prefere ser ímpar [digite i] ou par [digite p]? "))
        else:
            numero1 = int(input("Digite um número entre 1 e 10 para começar: "))
            numero2 = randint(1, 11)
            print(f'Meu número é {numero2}.')
            resultado = (numero1 + numero2) % 2
            print(f'A sobra da soma de {numero1} e {numero2} dá {resultado}.')
            if resultado == 0 and user == 'p':
                print('Você ganhou!')
                pontuacaouser += 1
            elif resultado != 0 and user == 'i':
                print('Você ganhou!')
                pontuacaouser += 1
            else:
                print('Você perdeu!')
                pontuacaomaquina += 1
            print(f'Pontuação: Você [ {pontuacaouser} ] vs [ {pontuacaomaquina} ] Máquina')
            jogo = input("Você quer continuar? Digite sim [s] ou não [n]. ").lower()
            if jogo != 's':
                break