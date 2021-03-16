#calculo de IMC

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura em m: "))
imc = peso / (altura ** 2)
print("IMC = {:.2f}.".format(imc))
if imc < 18.5:
    print("Seu IMC está ABAIXO do ideal. Procure um médico.")
elif imc >= 18.5 and imc < 25:
    print("Seu IMC está IDEAL.")
else:
    print("Seu IMC está ACIMA do ideal. Procure um médico.")