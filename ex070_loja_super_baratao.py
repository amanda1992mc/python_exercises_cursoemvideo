# Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos.
# No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato

total = 0
maiscaro = 0
maisbarato = 0
barato = ''
cont = ''
c = 0

while True:
    produto = str(input("Digite o nome do produto que vai comprar: "))
    preco = float(input("Digite o preço do produto: "))
    total += preco
    c += 1
    if preco > 1000:
        maiscaro = preco
    if c == 1 or preco < maisbarato:
        maisbarato = preco
        barato = produto
    cont = ' '
    while cont not in 'NS':
        cont = str(input("Você quer comprar mais algum produto? Digite [S] ou [N]: ")).upper()
    if cont == 'N':
        break
print(f'''O produto mais caro custa {maiscaro},
o mais barato é o {barato} que custa {maisbarato}.
No total você comprou {c} produtos que deu R${total:.2f}''')
