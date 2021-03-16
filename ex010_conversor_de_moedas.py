#conversor de moedas

dolar = float(input('Digite o valor do dolar hoje: '))
euro = float(input('Digite o valor do euro hoje: '))
real = float(input("Digite o valor em reais para saber seu valor em dolar e euro: "))

result = print("R${} valem {:.2f} dólares e {:.2f} euros.".format(real,(real/dolar),(real/euro)))



