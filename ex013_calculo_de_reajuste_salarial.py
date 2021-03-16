# calculo de reajuste salarial

aumento=float(input("Digite o percentual de aumento que incidirá sobre o salário: "))
salario=float(input("Digite o valor do salário base atual para o calculo: "))
valorfinal=(salario+((aumento/100)*salario))

print("O valor final do salário com aumento de {}% passará de R${:.2f} para R${:.2f}.".format(aumento,salario,valorfinal))