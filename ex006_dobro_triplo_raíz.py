#calculo de dobro, triplo e raiz quadrada de um input

n = int(input("Digite um número: "))
dobro = n * 2
triplo = n * 3
sr = n ** (1/2)
exp = n ** 2

print('O dobro de {} é igual a {}, o triplo é igual a {},\ne a raíz quadrada é {:.2f}'.format(n, dobro, triplo, sr))

n2 = int(input('Agora digite outro número para fazermos outras operações: '))

soma = n + n2
subtracao = n - n2
multiplicação = n * n2
divisão = n / n2
dint = n // n2
resto = n % n2

print('A soma é igual a {}, a subtração é igual {}, a multiplicação é igual a {}, a divisão é igual a {:.2f}, '
      'sendo o inteiro {} e o resto {}'.format(soma, subtracao, multiplicação, divisão, dint, resto))




