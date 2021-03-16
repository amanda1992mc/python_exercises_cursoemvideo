#validação de input

sexo = str(input("Informe seu sexo: [F | M] ")).upper().strip()[0]
while sexo != 'F' and sexo != 'M':
    sexo = str(input("Dado inválido. Tente novamente.")).upper().strip()[0]
print("Ok, você é do sexo {}.".format(sexo))