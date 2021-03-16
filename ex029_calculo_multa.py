#leia a velocidade enviada pelo radar e calcule se há multa e seu valor por km adicional
#é multado a partir de 80km/h, sendo R$7 cada km acima disso

vel = int(input("Digite a velocidade do veículo: "))
if vel <= 80:
    print("Parabéns! Você não estava acima do limite de velocidade e não foi multado.")
else:
    print("Você ultrapassou o limite de velocidade e terá que pagar uma multa de R${:.2f}".format((vel-80)*7))
