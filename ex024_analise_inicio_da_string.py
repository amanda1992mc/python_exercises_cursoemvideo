# Análise de Início da string
# Ao digitar o nome de uma cidade, responda se ela começa com santo.

cid = str(input("Digite o nome da cidade que você nasceu: ")).strip().upper().split()
print(cid[0]=='SANTO')