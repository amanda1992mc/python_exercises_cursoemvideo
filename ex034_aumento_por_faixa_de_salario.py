#pergunta o valor do salário e analisa o valor do aumento de acordo, sendo:
#até 1250 um aumento de 15%, mais que isso, aumento de 10%

salary = int(input("Digite o valor do seu salário atual: "))
if salary <= 1250:
    print("O seu aumento será de 15% sobre {}, que resulta em {}.".format(salary,salary+(salary*0.15)))
else:
    print("O seu aumento será de 10% sobre {}, resultando no valor bruto final de {}.".format(salary,(salary+(salary*0.10))))
