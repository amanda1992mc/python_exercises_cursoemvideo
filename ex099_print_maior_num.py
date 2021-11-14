

from time import sleep

def maior(* num):
    cont = maior = 0
    print('\n Analisando os números passados... ')
    sleep(1)
    for valor in num:
        print(f'{valor}', end=' ')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f"Foram informados {cont} números.")
    print(f"O maior valor informado foi {maior}.")



maior(1,2,3,4,5,6,9)