#pintando paredes

altura = float(input("Digite a altura da parede em metros: "))
largura = float(input("Digite a largura da parede em metros: "))
litro = 2
dimensao = altura * largura
tinta = dimensao/litro
print("A dimensão da sua parede é de {}m².".format(dimensao))
print("A quantidade de tinta necessária para pintar essa área é de {:.2f} litros.".format(tinta))

