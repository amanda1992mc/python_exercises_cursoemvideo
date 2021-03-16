#classificação de atletas por faixa de idade

from datetime import date
data = int(input("Digite seu ano de nascimento: "))
age = date.today().year
idade = (age - data)

# idade = int(input("Digite sua idade: "))

if idade <= 9:
    print("Classificação por idade: Mirim")
elif idade <= 14:
    print("Classificação por idade: Infantil")
elif idade <= 19:
    print("Classificação por idade: Junior")
elif idade <= 25:
    print("Classificação por idade: Adulto")
elif idade > 25:
    print("Classificação por idade: Sênior")
else:
    print("Inválido, tente novamente.")