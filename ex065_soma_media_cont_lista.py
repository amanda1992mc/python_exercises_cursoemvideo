#guarde inputs numa lista e mostre sua média, soma e contagem

num = []
resp = 's'
cont = 0
med = 0

while resp == 's':
    num.append(int(input("Digite um número: ")))
    resp = input("Quer continuar? [s] ou [n] ").lower()
    cont += 1
num.sort()
med = sum(num) / cont
print(f'Você digitou {cont} números, o menor é {num[0]}, o maior é {num[-1]}, a média é {med} e a soma é {sum(num)}.')
