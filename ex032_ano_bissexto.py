#script que analisa se o ano enviado é bissexto

from _datetime import date
ano = int(input("""Digite um ano para saber se ele é bissexto: 
Obs: Digite 0 para analisar o ano atual.
"""))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano {} é bissexto.".format(ano))
else:
    print("O ano {} não é bissexto.".format(ano))
