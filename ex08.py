################################################################
# Descrição: Apresenta a soma dos cem primeiros números        #
#            naturais (1+2+3+...+100).                         #
# Parâmetros de entrada: Nenhum                                #
# Valores de saída:      O valor total da soma                 #
# Autor:                 [Seu Nome Completo]                   #
################################################################

soma = 0
for i in range(1, 101):
    soma += i

print(f"A soma dos cem primeiros números naturais é: {soma}")
