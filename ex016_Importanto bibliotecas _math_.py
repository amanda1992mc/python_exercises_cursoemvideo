#módulos: raíz quadrada, arredondamento, parte inteira e decimal.


import math
num=float(input("Digite um número: "))
print("A raíz quadrada de {} é {}, arredondada para cima é {} e para baixo é {}.".format(num, math.sqrt(num),math.ceil(num),math.floor(num)))
print("A parte inteira de {} é igual a {}.".format(num,math.trunc(num)))

