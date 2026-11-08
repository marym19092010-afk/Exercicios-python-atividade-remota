################################################################
# Descrição: Apresenta todos os valores numéricos inteiros     #
#            ímpares situados na faixa de 0 a 20.              #
# Parâmetros de entrada: Nenhum                                #
# Valores de saída:      Números ímpares de 0 a 20             #
# Autor:                 [Seu Nome Completo]                   #
################################################################

print("Números ímpares de 0 a 20:")
for i in range(0, 21):
    if i % 2 != 0:
        print(i)
