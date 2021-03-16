#pergunte a distância da viagem, calcula e passagem sendo:
#R$050 por viagens de até 200km e R$0,45 por viagens maiores que 200 km.

km = int(input("Digite a distância da viagem em km: "))
if km <= 200:
    print("O valor da sua viagem será de R${:.2f}.".format(km*0.50))
else:
    print("O valor da sua viagem será de R${}.".format(km*0.45))