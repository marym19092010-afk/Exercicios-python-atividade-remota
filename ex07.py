################################################################
# Descrição: Mostra a tabuada tradicional de um número        #
#            qualquer fornecido pelo usuário.                  #
# Parâmetros de entrada: Um número inteiro para a tabuada      #
# Valores de saída:      Tabuada do número de 1 a 10           #
# Autor:                 [Seu Nome Completo]                   #
################################################################

numero = int(input("Digite um número para ver a tabuada: "))

print(f"--- Tabuada do {numero} ---")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
