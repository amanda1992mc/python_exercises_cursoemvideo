#soma de inputs com exceção

c = 0
n = 0
while True:
    f = int(input("Digite um número ou 999 para sair: "))
    if f == 999:
        break
    c += 1
    n += f
print(f'Foram impressos {c} números que somam {n}.')