# Exercício Python 083: Crie um programa onde o usuário digite
# uma expressão qualquer que use parênteses. Seu aplicativo deverá
# analisar se a expressão passada está com os parênteses abertos e
# fechados na ordem correta.

exp = str(input("Digite uma expressão matemática para validar: "))
count1 = []
count2 = []
p = ['(',')']
for p in exp:
    if p == '(':
        count1.append(p)
    if p == ')':
        count2.append(p)
if len(count1) == len(count2):
    print('Essa expressão matemática é válida.')
else:
    print('Essa expressão matemática é inválida.')
