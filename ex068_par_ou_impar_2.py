from random import randint
import sys

pontuacao_user = 0
pontuacao_maquina = 0

while True:
    jogo = input("Vamos brincar de Par ou Ímpar? Digite sim [s] ou não [n]. ").lower()

    if jogo == 'n':
        print('Finalizando programa... Bye :)')
        sys.exit(1)

    elif jogo == 's':
        while True:
            escolha_user = str(input(
                "Você prefere ser Par [digite p] ou Ímpar [digite i] ? (Digite 99 para encerrar o jogo) ")).lower()

            if escolha_user == '99':
                print("Finalizando programa... Bye :)")
                sys.exit(1)

            elif escolha_user != 'p' and escolha_user != 'i':
                print("Resposta inválida. Tente novamente!\n")
            else:
                while True:
                    numero_user = int(input("Digite um número entre 1 e 10 para começar: "))
                    if numero_user == '' or numero_user < 1 or numero_user > 10:
                        print('Valor inválido. Tente novamente!')
                    else:
                        numero_maquina = randint(1, 11)
                        resultado = (numero_user + numero_maquina) % 2

                        print(f'\nVamos lá... Seu número é {numero_user} e o meu é {numero_maquina}')
                        print(f'A sobra da soma de {numero_user} e {numero_maquina} dá {resultado}.\n')

                        if (resultado == 0 and escolha_user == 'p') or (resultado == 1 and escolha_user == 'i'):
                            print("Parabéns, você ganhou!")
                            pontuacao_user += 1
                        else:
                            print('Que pensa, você perdeu!')
                            pontuacao_maquina += 1

                        print('\n#########################################')
                        print(f'Pontuação: Você [{pontuacao_user}] vs Máquina [{pontuacao_maquina}]')
                        print('###########################################\n')

                        while True:
                            jogo = input("Você quer continuar? Digite sim [s] ou não [n]. ").lower()
                            if jogo == 'n':
                                sys.exit(1)
                            elif jogo == 's':
                                print("Legal, vamos jogar outra partida!")
                                break
                            else:
                                print("Resposta inválida. Tente novamente!\n")
    else:
        print('Não entendi sua resposta. Vamos tentar de novo :)')