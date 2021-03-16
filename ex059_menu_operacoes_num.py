#menu de opções de cálculos

n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))
opção = 0
while opção != 5:
    print('''
    [1] Somar
    [2] Multiplicar
    [3] Saber o maior
    [4] Digitar novos números
    [5] Sair do Programa
    ''')
    opção = int(input("O que você quer fazer com os números? Digite o código correspondente: "))
    if opção == 1:
        print("A soma de {} e {} é {}.".format(n1,n2,n1+n2))
    elif opção == 2:
        print("A multiplicação de {} e {} é {}.".format(n1,n2,n1*n2))
    elif opção == 3:
        if n1 > n2:
            print("O maior entre {} e {} é {}.".format(n1,n2,n1))
        elif n2 > n1:
            print("O maior entre {} e {} é {}.".format(n1,n2,n2))
        else:
            print("Os números são iguais.")
    elif opção == 4:
        n1 = int(input("Digite um valor: "))
        n2 = int(input("Digite outro valor: "))
    elif opção > 5:
        print("Opção inválida. Tente novamente.")
else:
    print("Você optou por sair do programa. Obrigada e volte sempre!")
print('finalizado')



