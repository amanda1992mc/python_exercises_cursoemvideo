#Interagir com o usuário: perguntar e retornar input

#opção 1
nome = input('Qual é seu nome? ')
print('Bem vindo(a),',nome,'!')

#opção 2
#mais indicado, mais fácil de adicionar diversas variáveis

nome = input('Qual o é seu nome?')
print('Seja bem vindo(a),{}!'.format(nome))