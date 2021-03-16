#conversão de bases numéricas

num1 = int(input("Digite o número que você quer que seja convertido: "))
base = int(input("Digite o número referente a base para qual você quer converter o número:\n"
             "1 - binário\n"
             "2 - octal\n"
             "3 - hexadecimal\n"))
if base == 1:
    print('O número {} em binário é {}.'.format(num1,bin(num1)[2:]))
elif base == 2:
    print('O número {} em octal é {}.'.format(num1, oct(num1)[2:]))
elif base == 3:
    print('O número {} em hexadecimal é {}.'.format(num1, hex(num1)[2:]))
else:
    print("O valor digitado não corresponde a nenhuma das bases numéricas sugeridas.")