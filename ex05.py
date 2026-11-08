################################################################
# Descrição: Calcula a média de duas notas parciais e exibe a  #
#            situação do aluno.                                #
# Parâmetros de entrada: Duas notas parciais do aluno          #
# Valores de saída:      Aprovado, Reprovado ou Aprovado com   #
#                        Distinção                             #
# Autor:                 [Seu Nome Completo]                   #
################################################################

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media == 10:
    print("Aprovado com Distinção")
elif media >= 7:
    print("Aprovado")
else:
    print("Reprovado")
