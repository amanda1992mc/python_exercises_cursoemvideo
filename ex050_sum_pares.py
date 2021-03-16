#soma de pares no range

cont = 0
soma = 0
for c in range(1,7):
    num = int(input("Digite o {}º valor: ".format(c)))
    cont += 1
    if num % 2 == 0:
        soma += num
print("Você digitou {} valores e a soma dos pares é {}.".format(cont,soma))