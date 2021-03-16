#analise/ receber um input e analisar tipo de variável e algumas de suas propriedades

str = input("Digite o que deve ser analisado: ")

#type() e len() são funções enquanto os outros são métodos:

print("Esse valor está sendo coletado e armazenado como", type(str))
print("É um texto? ",str.isalpha())
print("Contém letras e números? ", str.isalnum())
print("Contem apenas espaço? ", str.isspace())
print("É numérico? ",str.isalnum())
print("É decimal? ",str.isdecimal())
print('Tem {} caracteres.'.format((len(str))))
