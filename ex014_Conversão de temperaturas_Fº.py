#conversor de temperaturas
#cls=(((frh-32)*5)/9)

cls=float(input("Digite a temperatura em Cº para ver o valor em F°: "))
frh=(((cls*9)/5)+32)

print("A temperatura {}C° é equivalente a {}F°.".format(cls,frh))
