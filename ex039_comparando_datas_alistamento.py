#analise de idade para aistamento

import datetime
nasc = int(input("Digite o ano do seu nascimento: "))
sexo = str(input("Você é do sexo masculino ou feminino? Por favor digite: "))
atual = datetime.date.today().year
idade = atual - nasc
print("Quem nasceu em {} tem {} anos em {}.".format(nasc, idade, atual))
if sexo == "masculino":
    if idade == 18:
        print("Você deve se alistar esse ano.")
    elif idade < 18:
        print("Faltam {} anos para bocê se alistar.".format(18-idade))
    else:
        print("Você já passou dos 18 anos e deve ter feito o alistamento")
elif sexo == "feminino":
    print("Sendo do sexo feminino você não precisa se alistar.")
else:
    print("Alguma informação digitada é invalida. Por favor tente novamente.")