#quebrando e analisando a string

nome = str(input("Escreva seu nome inteiro: ")).strip()
n = nome.split()
print("Olá, ", nome)
print("Seu primeiro nome é: {}.".format(n[0]))
print("Seu último nome é: {}".format(n[-1]))

