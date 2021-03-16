#calculo de seno, coseno e tangente de ângulo

import math
ang = float(input("Digite um ângulo que precisa ter suas medidas cauculadas: "))
cos = math.cos(math.radians(ang))
seno = math.sin(math.radians(ang))
tang = math.tan(math.radians(ang))
print("O seno do ângulo {} é {:.2f}, o coseno é {:.2f} e a tangente é {:.2f}.".format(ang,seno,cos, tang))
