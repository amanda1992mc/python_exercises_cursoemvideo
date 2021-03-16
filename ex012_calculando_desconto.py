#calculando descontos %

desconto=float(input("Insira o valor do desconto: "))
produto=float(input("Digite o preço do produto: "))
valorfinal=(produto-(desconto/100))

print("O valor final aplicado o desconto é de R${}.".format(valorfinal))
