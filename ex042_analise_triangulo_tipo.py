#analise das dimensões e tipo de triângulo

m1 = int(input("Digite a primeira medida para seu triângulo: "))
m2 = int(input("Digite a segunda medida para seu triângulo: "))
m3 = int(input("Digite a terceira medida para seu triângulo: "))
if m1 < m2 + m3 and m2 < m1+m3 and m3 < m1+m2:
    print("Essas medidas podem formar um triângulo escaleno!")
elif m1 == m2 and m2 == m3:
    print("Essas medidas podem formar um triângulo equilátero!")
elif m1 == m2 and m1 == m3 or m2 == m3:
    print("Essas medidas podem formar um triângulo isósceles!")
else:
    print("Essas medidas não podem formar um triângulo.")