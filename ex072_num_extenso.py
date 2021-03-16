tupla = ('zero','um', 'dois','três','quatro','cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
         'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n = 0
while True:
    n = int(input("Digite um número entre 0 e 20: "))
    if n < 20 and n >= 0:
        print(f'O número {n} por extenso é {tupla[n]}.')
    if n > 20:
        break
print("FIM")
