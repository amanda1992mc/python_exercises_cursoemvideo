# Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras
# (não usar acentos). Depois disso, você deve mostrar, para cada palavra,
# quais são as suas vogais.

texto = str(input("Digite uma frase para contarmos quantas vogais ela tem: "))

qtdevogais = 0

for aeiou in texto:
    qtdevogais += 1

print(f"O texto digitado tem {qtdevogais} vogais")