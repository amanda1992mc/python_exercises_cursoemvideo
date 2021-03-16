#analise de média e aprovação/reprovação

n1 = float(input("Digite sua primeira nota com decimais: "))
n2 = float(input("Digite sua segunda nota com decimais: "))
media = n1 + n2 / 2
if media <= 5:
    print("Você foi reprovado :( ")
elif media >= 5 < 7:
    print("Você ficou de recupeação e aidna tem uma chance de passar. Estude mais!")
else:
    print("Você foi aprovado! :D")