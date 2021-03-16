#calculo de catetos e hipotenusa

import math

co = float(input("Digite o valor do cateto oposto: "))
ca = float(input("Digite o valor do cateto adjacente: "))

'''sem importação'''
hip = (((co**2)+(ca**2))**(1/2))
print("A hipotenusa mede ", hip)

'''com importação'''
hyp = math.hypot(co,ca)
print("A hipotenusa vale {:.1f}".format(hyp))