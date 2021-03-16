#some quantos numeros receber menos o último

n = 0
nf = 0
while n != 999:
    n = int(input("Digite um número para adicionar a soma ou 999 para encerrar: "))
    if n != 999:
        nf += n
print(f"A soma dos números digitados é {nf}")