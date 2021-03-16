#análise de números (milhares, centenas, dezenas e unidades)

n = int(input("Digite um número de quatro dígitos: "))
m = n // 1000
c = n // 100 % 10
d = n // 10 % 10
u = n % 10
print('O número é composto por {} milhar(es), {} centena(s), {} dezena(s) e {} unidade(s).'.format(m,c,d,u))
