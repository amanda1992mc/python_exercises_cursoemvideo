#aprovação de emprestimo

salario = int(input("Digite seu salário: "))
casa = int(input("Digite o valor da casa para ser financiado: "))
prazo = int(input("Digite o prazo de pagamento desejado em anos: "))

if casa / (prazo * 12) <= (salario * 0.30):
    print("Seu empréstimo foi aprovado!A parcela será de R${:.2f} em {} vezes.".format((casa/(prazo*12)),(prazo*12)))
else:
    print("Seu empréstimo não foi aprovado. De acordo com seus dados,\n"
          "o prazo precisa ser de {:.1f} anos".format(casa/((salario*0.30)*12)))
