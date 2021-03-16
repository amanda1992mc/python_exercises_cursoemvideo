#calculo de desconto conforme valor da compra e forma de pgto

compra = int(input("Digite o valor da compra: "))
pgto = int(input('''
Digite a forma de pagamento desejada:
[1] a vista - transferência bancária ou débito online
[2] a vista cartão de crédito
[3] Parcelado no cartão 
'''))
if pgto == 1:
    print("A sua compra de R${} terá R${} de desconto e sairá por R${}.".format(compra, '10%', (compra - (compra * 0.10))))
elif pgto == 2:
    print("A sua compra de R${} terá R${} de desconto e sairá por R${}.".format(compra, '5%', (compra - (compra * 0.05))))
elif pgto == 3:
    print("A sua compra de R${} terá R${} de juros e sairá por R${}.".format(compra, '10%', (compra + (compra * 0.10))))