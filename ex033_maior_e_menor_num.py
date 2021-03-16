#programa que lê 3 números diferentes e aponta o maior e o menor

num1 = int(input("Digite três números: "))
num2 = int(input("Digite outro número: "))
num3 = int(input("Digite apenas mais um número: "))
gr = [num1, num2, num3]
print("O maior número é {} e o menor é {}.".format(max(gr),min(gr)))