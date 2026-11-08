################################################################
# Descrição: Programa que pede dois números e imprime o maior. #
# Parâmetros de entrada: Dois números digitados pelo usuário   #
# Valores de saída:      O maior número entre os dois          #
# Autor:                 [Seu Nome Completo]                   #
################################################################

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if num1 > num2:
    print(f"O maior número é: {num1}")
elif num2 > num1:
    print(f"O maior número é: {num2}")
else:
    print("Os dois números são iguais.")
