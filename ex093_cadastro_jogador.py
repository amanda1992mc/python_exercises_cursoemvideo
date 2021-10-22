#Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador
#de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou.
#Depois vai ler a quantidade de gols feitos em cada partida.
#No final, tudo isso será guardado em um dicionário,
#incluindo o total de gols feitos durante o campeonato.


jogador = dict()
partidas = 0
gols = list()


jogador['nome'] = input("Qual o nome do jogador que vamos cadastrar? ")
partidas = int(input(f"Quantas partidas ele(a) jogou? "))
for i in range(1, partidas+1):
    gols.append(int(input(f"Quantos gols {jogador['nome']} fez na {i} partida? ")))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)

print(jogador)

for k,v in jogador.items():
    print(f"O campo {k} tem o valor {v}.\n")

print(f'O jogador {jogador["nome"]} jogou {partidas} partidas e fez {jogador["total"]} gols. \n')

for i,v in enumerate(jogador["gols"]):
    print(f"Na partida {i+1} o jogador fez {v} gols.")