#numeros primos


num = int(input("Digite o número para ver se ele é primo: "))
c = 0
for e in range(1, num+1):
    if num % e == 0:
        print(e)
        c += 1
if c == 2:
    print("\nO número {} é primo.".format(num))
else:
    print("\nO número {} não é primo.".format(num))
