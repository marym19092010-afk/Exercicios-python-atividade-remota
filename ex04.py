################################################################
# Descrição: Pergunta o turno de estudo e exibe a saudação     #
#            correspondente.                                   #
# Parâmetros de entrada: Letra do turno (M, V ou N)            #
# Valores de saída:      Bom Dia!, Boa Tarde!, Boa Noite! ou   #
#                        Valor Inválido!                       #
# Autor:                 [Seu Nome Completo]                   #
################################################################

turno = input("Em que turno você estuda? (M - Matutino / V - Vespertino / N - Noturno): ").strip().upper()

if turno == 'M':
    print("Bom Dia!")
elif turno == 'V':
    print("Boa Tarde!")
elif turno == 'N':
    print("Boa Noite!")
else:
    print("Valor Inválido!")
