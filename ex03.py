################################################################
# Descrição: Verifica se a letra digitada é 'F' ou 'M' e       #
#            informa o sexo correspondente.                    #
# Parâmetros de entrada: Uma letra ('F' ou 'M')                #
# Valores de saída:      F - Feminino, M - Masculino ou Sexo   #
#                        Inválido                              #
# Autor:                 [Seu Nome Completo]                   #
################################################################

letra = input("Digite a letra (F ou M): ").strip().upper()

if letra == 'F':
    print("F - Feminino")
elif letra == 'M':
    print("M - Masculino")
else:
    print("Sexo Inválido")
