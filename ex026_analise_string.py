#primeira e última ocorrência de um elemento na string


frase = str(input("Digite uma frase: ")).strip().lower()

print("A letra A aparece {} vezes na frase.".format(frase.count('a')))

print("A letra A apareceu pela primeira vez na posição {}.".format(frase.find('a')))

print("A letra A apareceu pela última vez na posição {}.".format(frase.rfind('a')))