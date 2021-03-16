#calculo de custo final de aluguel de carros

dias=int(input("Digite a quantidade de dias que você ficou com o carro: "))
km=float(input("Digite o total de quiilometros rodados com o carro alugado nesse período: "))
custo=((dias*60)+(km*0.15))
print("O custo final do aluguel somando-se as diárias e a quilometragem é de R${:.2f}.".format(custo))

