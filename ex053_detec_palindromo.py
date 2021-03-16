#ver se a frase é igual de invertida

frase = str(input("Digite uma frase para ver se ela é um palindromo: ")).strip().upper().split()
print(frase)
if frase == frase[::-1]:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")