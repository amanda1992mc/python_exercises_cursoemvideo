#Análise de caracteres da string

#nesse primeiro código, o .split já tira os espaços desnecessários que podem ser enviados pelo usuário
nome = str(input("Digite seu nome completo: ")).strip()

print('Seu nome em maiúsculas é {}.'.format(nome.upper()))
print('Seu nome em minúsculas é {}.'.format(nome.lower()))

#nesse comando estamos somando todos os caracteres e subtraindo a quantidade que é referente a espaços
print('Seu nome contém {} caractéres.'. format(len(nome) - nome.count(' ')))

#Nesse comando, precisamos contar apenas o primeiro nome. Primeiro foi feito  a separação das cadeias de caracteres
#por padrão o slipt tem espaços como separador
separa = nome.split()

#ao separar as cadeias de texto, o 1º nome tem índice zero
#aqui chamamos o item de índice 0 e contamos seus caractéres
print('Seu primeiro nome é {} e ele tem {} caractéres.'.format(separa[0],len(separa[0])))

print("A letra a minúscula aparece {} vezes no seu nome inteiro.".format(nome.count('a')))